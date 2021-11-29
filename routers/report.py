from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.param_functions import Path
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.point import Point
from models.path import Path
from models.report import Report, ReportCreate, ReportRead, ReportReadWithPathAndPoints
from utils.handle_errors import handle_integrity_error


router = APIRouter(
    prefix="/reports",
    responses={404: {"description": "Not found"}},
    tags=["reports"]
)

@router.get('/{organization_id}', response_model=List[ReportReadWithPathAndPoints])
async def read_reports(organization_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point, Path, Report).where(Report.organization_id == organization_id and Report.id == Path.report_id and Path.id == Point.path_id)
    result = await session.execute(statement)

    reports = result.scalars().all()
    return reports

@router.get('/report/{report_id}', response_model=ReportReadWithPathAndPoints)
async def read_report(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point, Path, Report).where(Report.id == report_id and Report.id == Path.report_id and Path.id == Point.path_id)
    result = await session.execute(statement)

    report = result.scalar_one_or_none()
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return report

@router.post('/report', status_code=status.HTTP_201_CREATED)
async def create_report(report: ReportCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_report = Report.from_orm(report)
        session.add(db_report)
        await session.flush()
        await session.refresh(db_report)

        path = report.path
        path.report_id = db_report.id

        db_path = Path.from_orm(path)
        session.add(db_path)
        await session.flush()
        await session.refresh(db_path)

        points = path.points
        for point in points:
            point.path_id = db_path.id
            db_point = Point.from_orm(point)
            session.add(db_point)

        await session.flush()

    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_report
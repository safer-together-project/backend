from os import error
from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.report import Report, ReportCreate, ReportRead
from utils.handle_errors import handle_integrity_error


router = APIRouter(
    prefix="/reports",
    responses={404: {"description": "Not found"}},
    tags=["reports"]
)

@router.get('/{organization_id}', response_model=List[ReportRead])
async def read_reports(organization_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Report).where(Report.organization_id == organization_id)
    result = await session.execute(statement)

    reports = result.scalars().all()
    return reports

@router.get('/report/{report_id}', response_model=ReportRead)
async def read_report(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Report).where(Report.id == report_id)
    result = await session.execute(statement)

    report = result.scalar_one_or_none()
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return report

@router.post('/report/', status_code=status.HTTP_201_CREATED)
async def create_report(report: ReportCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_report = Report.from_orm(report)
        session.add(db_report)
        await session.flush()
        await session.refresh(db_report)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_report
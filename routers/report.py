from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.report import Report, ReportCreate, ReportRead


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
        session.add(report)
        await session.flush()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Report already created with the same id.")
    else:
        await session.commit()
    return report
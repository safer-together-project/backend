from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.beacon import Beacon
from models.report import Report


router = APIRouter(
    prefix="/reports",
    responses={404: {"description": "Not found"}},
    tags=["reports"]
)

@router.get('/{organization_id}', response_model=List[Report])
async def read_reports(organization_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Report).where(Report.organization_id == organization_id)
    result = await session.execute(statement)

    reports = result.all()
    return reports

@router.get('/report/{report_id}', response_model=Report)
async def read_report(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Report).where(Report.id == report_id)
    result = await session.execute(statement)

    report = result.first()
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return report
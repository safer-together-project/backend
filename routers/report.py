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

@router.get('/{organization_id}', response_model=list[Report])
async def read_reports(organization_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Report).where(Report.organization_id == organization_id)
    result = session.exec(statement)

    reports = result.scalar().all()
    return reports

@router.get('/report/{report_id}', response_model=Report)
async def read_report(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Beacon).where(Beacon.id == report_id)
    result = session.exec(statement)

    report = result.scalar().first()
    if report is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return report
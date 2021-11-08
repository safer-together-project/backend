from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from core.database import get_db
from models.report import Report
from schemas.report import ReportBase

router = APIRouter(
    prefix="/reports",
    responses={404: {"description": "Not found"}},
    tags=["reports"]
)

@router.get('/{organization_id}', response_model=List[ReportBase])
async def read_reports(organization_id: str, db: Session = Depends(get_db)):
    reports = db.query(Report).filter(Report.organization_id == organization_id)

    return [ReportBase(
                id=report.id, 
                organization_id=report.organization_id, 
                infection_type=report.infection_type) for report in reports]

@router.get('/report/{report_id}', response_model=ReportBase)
async def read_report(report_id: str, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id)

    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return ReportBase(
                id=report.id, 
                organization_id=report.organization_id, 
                infection_type=report.infection_type)
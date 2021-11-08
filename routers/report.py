from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from core.database import get_db
from models.report import Report
from schemas.report import ReportBase

router = APIRouter(
    prefix="/reports",
    responses={404: {"description": "Not found"}},
)

@router.get('/{organization_id}', response_model=ReportBase, tags=["report"])
async def read_reports(organization_id: str, db: Session = Depends(get_db)):
    reports = db.query(Report).filter(Report.organization_id == organization_id)

    return [ReportBase(
                id=report.id, 
                organization_id=report.organization_id, 
                infection_type=report.infection_type) for report in reports]
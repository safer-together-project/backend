from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from core.database import get_db
from models.path import Path
from schemas.path import PathBase

router = APIRouter(
    prefix="/path",
    responses={404: {"description": "Not found"}},
)

@router.get('/{report_id}', response_model=PathBase, tags=["path"])
async def read_path(report_id: str, db: Session = Depends(get_db)):
    path = db.query(Path).filter(Path.report_id == report_id).first()

    if path is None:
        raise HTTPException(status_code=404, detail="Path not found")

    return PathBase(
                id=path.id, 
                report_id=path.report_id)
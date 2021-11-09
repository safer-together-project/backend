from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from core.db import get_session
from models.path import Path

router = APIRouter(
    prefix="/path",
    responses={404: {"description": "Not found"}},
    tags=["path"]
)

@router.get('/{report_id}', response_model=Path)
async def read_path(report_id: str, session: Session = Depends(get_session)):
    with session:
        statement = select(Path).where(Path.report_id == report_id)
        result = session.exec(statement)

        path = result.first()
        if path is None:
            raise HTTPException(status_code=404, detail="Organization not found")

        return path

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.path import Path

router = APIRouter(
    prefix="/path",
    responses={404: {"description": "Not found"}},
    tags=["path"]
)

@router.get('/{report_id}', response_model=Path)
async def read_path(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Path).where(Path.report_id == report_id)
    result = await session.execute(statement)

    path = result.scalar_one_or_none()
    if path is None:
        raise HTTPException(status_code=404, detail="Path not found")

    return path

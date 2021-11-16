from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from utils.handle_errors import handle_integrity_error
from core.db import get_session
from models.path import Path, PathCreate, PathRead

router = APIRouter(
    prefix="/path",
    responses={404: {"description": "Not found"}},
    tags=["path"]
)

@router.get('/{report_id}', response_model=PathRead)
async def read_path(report_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Path).where(Path.report_id == report_id)
    result = await session.execute(statement)

    path = result.scalar_one_or_none()
    if path is None:
        raise HTTPException(status_code=404, detail="Path not found")

    return path

@router.post('', response_model=PathRead)
async def create_path(path: PathCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_path = Path.from_orm(path)
        session.add(db_path)
        await session.flush()
        await session.refresh(db_path)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_path
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.point import Point


router = APIRouter(
    prefix="/points",
    responses={404: {"description": "Not found"}},
    tags=["points"]
)

@router.get('/{path_id}', response_model=list[Point])
async def read_points(path_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point).where(Point.path_id == path_id)
    result = await session.exec(statement)

    points = result.scalar().all()
    return points

@router.get('/point/{point_id}', response_model=Point)
async def read_point(point_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point).where(Point.id == point_id)
    result = await session.exec(statement)

    point = result.scalar().first()
    if point is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return point
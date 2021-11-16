from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.point import Point, PointCreate, PointRead
from utils.handle_errors import handle_integrity_error


router = APIRouter(
    prefix="/points",
    responses={404: {"description": "Not found"}},
    tags=["points"]
)

@router.post('', response_model=PointRead)
async def create_points(points: List[PointCreate], session: AsyncSession = Depends(get_session)):
    def map_to_orm(point):
        return Point.from_orm(point)

    try:
        db_points = map(map_to_orm, points)
        session.add_all(db_points)
        await session.flush()
        await session.refresh(db_points)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_points

@router.get('/{path_id}', response_model=List[PointRead])
async def read_points(path_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point).where(Point.path_id == path_id)
    result = await session.execute(statement)

    points = result.scalars().all()
    return points

@router.post('/point', response_model=List[PointRead])
async def create_point(point: PointCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_point = Point.from_orm(point)
        session.add(db_point)
        await session.flush()
        await session.refresh(db_point)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_point

@router.get('/point/{point_id}', response_model=PointRead)
async def read_point(point_id: str, session: AsyncSession = Depends(get_session)):
    statement = select(Point).where(Point.id == point_id)
    result = await session.execute(statement)

    point = result.scalar_one_or_none()
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")

    return point
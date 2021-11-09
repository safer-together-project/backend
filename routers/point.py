from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from core.database import get_session
from models.point import Point


router = APIRouter(
    prefix="/points",
    responses={404: {"description": "Not found"}},
    tags=["points"]
)

@router.get('/{path_id}', response_model=List[Point])
async def read_points(path_id: str, session: Session = Depends(get_session)):
    with session:
        statement = select(Point).where(Point.path_id == path_id)
        result = session.exec(statement)

        points = result.all()
        return points

@router.get('/point/{point_id}', response_model=Point)
async def read_point(point_id: str, session: Session = Depends(get_session)):
    with session:
        statement = select(Point).where(Point.id == point_id)
        result = session.exec(statement)

        point = result.first()
        if point is None:
            raise HTTPException(status_code=404, detail="Organization not found")

        return point
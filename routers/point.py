from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from core.database import get_db

from models.point import Point
from schemas.path import PathBase
from schemas.point import PointBase

router = APIRouter(
    prefix="/points",
    responses={404: {"description": "Not found"}},
)

@router.get('/{path_id}', response_model=List[PointBase], tags=["points"])
async def read_points(path_id: str, db: Session = Depends(get_db)):
    points = db.query(Point).filter(Point.path_id == path_id)
    return [PathBase(
                id=point.id, 
                beacon_id=point.beacon_id,
                coordinates_id=point.coordinates_id,
                path_id=point.path_id,
                initial_timestamp=point.initial_timestamp,
                final_timestamp=point.final_timestamp,
                longitude=point.longitude,
                latitude=point.latitude) for point in points]

@router.get('/point/{point_id}', response_model=PointBase, tags=["point"])
async def read_beacon(point_id: str, db: Session = Depends(get_db)):
    point = db.query(Point).filter(Point.id == point_id).first()
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")

    return PathBase(
                id=point.id, 
                beacon_id=point.beacon_id,
                coordinates_id=point.coordinates_id,
                path_id=point.path_id,
                initial_timestamp=point.initial_timestamp,
                final_timestamp=point.final_timestamp,
                longitude=point.longitude,
                latitude=point.latitude)
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy.sql.schema import ForeignKeyConstraint
from sqlmodel import SQLModel, Field, Relationship
from pydantic.json import isoformat

if TYPE_CHECKING:
    from path import Path, PathRead
    from beacon import Beacon, BeaconRead

class PointBase(SQLModel):
    __table_args__ = (ForeignKeyConstraint(["beacon_id", "beacon_major", "beacon_minor"], ["beacon.id", "beacon.major", "beacon.minor"]), )

    initial_timestamp: datetime = Field(index=True)
    initial_timestamp: datetime = Field(index=True)
    final_timestamp: datetime = Field(index=True)
    longitude: float = Field(index=True)
    latitude: float = Field(index=True)

    beacon_id: Optional[str] = Field(index=True, default=None, nullable=False, max_length=36)
    beacon_major: Optional[int] = Field(index=True, default=None, nullable=False)
    beacon_minor: Optional[int] = Field(index=True, default=None, nullable=False)
    path_id: Optional[int] = Field(index=True, default=None, foreign_key="path.id")

    class Config:
        json_encoders = {
            datetime: isoformat
        }

class Point(PointBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    path: Optional["Path"] = Relationship(back_populates="points")
    beacon: Optional["Beacon"] = Relationship(back_populates=None)

class PointCreate(PointBase):
    pass

class PointRead(PointBase):
    id: int

class PointReadWithPath(PointBase):
    path: Optional["PathRead"] = None

class PointReadWithBeacon(PointBase):
    beacon: Optional["BeaconRead"] = None

class PointReadWithPathAndBeacon(PointBase):
    path: Optional["PathRead"] = None
    beacon: Optional["BeaconRead"] = None

class PointUpdate(SQLModel):
    id: Optional[int] = None
    initial_timestamp: Optional[datetime]
    final_timestamp: Optional[datetime]
    longitude: Optional[float]
    latitude: Optional[float]
    beacon_id: Optional[str] = None
    beacon_major: Optional[int] = None
    beacon_minor: Optional[int] = None
    path_id: Optional[int] = None


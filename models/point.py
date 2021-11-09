import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel.main import Relationship

from models.path import Path


class Point(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    beacon_id: Optional[int] = Field(default=None, foreign_key="Beacon.id")
    path_id: Optional[int] = Field(default=None, foreign_key="Path.id")
    initial_timestamp: datetime
    final_timestamp: datetime
    longitude: float
    latitude: float

    path: Optional[Path] = Relationship(back_populates="points")
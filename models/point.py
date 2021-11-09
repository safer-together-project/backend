from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from path import Path

class Point(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    beacon_id: Optional[int] = Field(default=None, foreign_key="Beacon.id")
    path_id: Optional[int] = Field(default=None, foreign_key="Path.id")
    initial_timestamp: datetime
    final_timestamp: datetime
    longitude: float
    latitude: float

    path: Optional["Path"] = Relationship(back_populates="points")
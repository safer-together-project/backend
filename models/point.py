from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from path import Path

class Point(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    beacon_id: Optional[str] = Field(default=None, foreign_key="beacon.id", max_length=35)
    path_id: Optional[int] = Field(default=None, foreign_key="path.id")
    initial_timestamp: datetime
    final_timestamp: datetime
    longitude: float
    latitude: float

    path: Optional["Path"] = Relationship(back_populates="points")
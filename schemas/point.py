from datetime import datetime
from pydantic import BaseModel

class PointBase(BaseModel):
    id: int
    beacon_id: int
    path_id: int
    initial_timestamp: datetime
    final_timestamp: datetime
    longitude: float
    latitude: float

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
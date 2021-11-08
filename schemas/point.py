from datetime import datetime
from pydantic import BaseModel

class PointBase(BaseModel):
    id: int
    beacon_id: int
    coordinates_id: int
    path_id: int
    initial_timestamp: datetime
    final_timestamp: datetime

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
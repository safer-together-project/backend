from typing import List
from pydantic import BaseModel


class BeaconBase(BaseModel):
    id: str
    organization_id: str
    location_id: str
    major: int
    minor: int
    status: int

    # Automatically translates from dict to object
    class Config:
        orm_mode = True

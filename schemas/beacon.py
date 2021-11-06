from typing import List
from pydantic import BaseModel


class BeaconBase(BaseModel):
    id: str
    organization_id: str
    major: int
    minor: int
    location: List[float]
    status: int

    # Automatically translates from dict to object
    class Config:
        orm_mode = True

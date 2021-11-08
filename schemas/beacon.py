from pydantic import BaseModel


class BeaconBase(BaseModel):
    id: str
    organization_id: int
    major: int
    minor: int
    status: int
    longitude: float
    latitude: float

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
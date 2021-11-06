from pydantic import BaseModel


class BeaconSchema(BaseModel):
    id: str
    organization_id: str
    major: int
    minor: int
    location: list[float]
    status: int

    # Automatically translates from dict to object
    class Config:
        orm_mode = True

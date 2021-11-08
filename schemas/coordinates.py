from pydantic import BaseModel


class CoordinatesBase(BaseModel):
    id: int
    longitude: float
    latitude: float

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
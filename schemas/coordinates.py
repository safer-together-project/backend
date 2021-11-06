from pydantic import BaseModel


class CoordinatesBase(BaseModel):
    id: str
    logitude: float
    lattitude: float

    # Automatically translates from dict to object
    class Config:
        orm_mode = True

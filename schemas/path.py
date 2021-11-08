from pydantic import BaseModel


class PathBase(BaseModel):
    id: int
    report_id: int

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
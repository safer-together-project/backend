from pydantic import BaseModel


class ReportBase(BaseModel):
    id: int
    organization_id: int
    infection_type: int

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
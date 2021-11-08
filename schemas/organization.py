from pydantic import BaseModel


class OrganizationBase(BaseModel):
    id: str
    name: str
    access_code: str

    # Automatically translates from dict to object
    class Config:
        orm_mode = True
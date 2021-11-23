from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from report import Report, ReportRead


class InfectionBase(SQLModel):
    name: str = Field(max_length=256)
    type: int
    description: str = Field(max_length=pow(2, 10))
    mandate_mask: bool


class Infection(InfectionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    reports: List["Report"] = Relationship(back_populates="infection")


# CRUD

class InfectionCreate(InfectionBase):
    pass


class InfectionRead(InfectionBase):
    id: int


class InfectionUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[int] = None
    description: Optional[str] = None
    mandate_mask: Optional[bool] = None
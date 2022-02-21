from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from infection_condition import InfectionCondition, InfectionConditionRead


class InfectionBase(SQLModel):
    name: str = Field(index=True, max_length=256)
    type: int = Field(index=True)
    description: str = Field(index=True, max_length=pow(2, 10))


class Infection(InfectionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    infection_conditions: List["InfectionCondition"] = Relationship(back_populates="infection")


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

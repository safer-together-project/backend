from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from infection import Infection, InfectionRead
    from organization import Organization
    from report import Report

class InfectionConditionBase(SQLModel):
    mask_required: bool = Field(index=True)
    distance: float = Field(index=True, default=3)
    duration: float = Field(index=True, default=60)

    organization_id: Optional[int] = Field(index=True, default=None, foreign_key="organization.id")
    infection_id: Optional[int] = Field(index=True, default=None, foreign_key="infection.id")


class InfectionCondition(InfectionConditionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(back_populates="infection_conditions")
    infection: Optional["Infection"] = Relationship(back_populates="infection_conditions")
    reports: List["Report"] = Relationship(back_populates="infection_condition")

# CRUD

class InfectionConditionCreate(InfectionConditionBase):
    pass


class InfectionConditionRead(InfectionConditionBase):
    id: int


class InfectionConditionReadWithInfection(InfectionConditionRead):
    infection: Optional["InfectionRead"] = None


class InfectionConditionUpdate(SQLModel):
    id: Optional[int] = None
    mask_required: Optional[bool] = None
    distance: Optional[float] = None
    duration: Optional[float] = None


from models.infection import InfectionRead
InfectionConditionCreate.update_forward_refs()
InfectionConditionRead.update_forward_refs()
InfectionConditionReadWithInfection.update_forward_refs()

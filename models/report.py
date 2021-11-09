from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization
    from path import Path

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    infection_type: int

    organization: Optional["Organization"] = Relationship(back_populates="reports")
    path: Optional["Path"] = Relationship(back_populates="report")
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization
    from path import Path

class ReportBase(SQLModel):
    infection_type: int

    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")

class Report(ReportBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(back_populates="reports")
    path: Optional["Path"] = Relationship(back_populates="report")

class ReportCreate(ReportBase):
    pass

class ReportRead(ReportBase):
    id: int

class ReportUpdate(SQLModel):
    infection_type: Optional[int] = None
    organization_id: Optional[int] = None


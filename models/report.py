from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization, OrganizationRead
    from path import Path, PathRead

class ReportBase(SQLModel):
    infection_type: int

    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")

class Report(ReportBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(back_populates="reports")
    path: Optional["Path"] = Relationship(back_populates="report")

# CRUD

class ReportCreate(ReportBase):
    pass

class ReportRead(ReportBase):
    id: int

class ReportReadWithPath(ReportRead):
    path: Optional["PathRead"] = None

class ReportReadWithOrganization(ReportRead):
    organization: Optional["OrganizationRead"] = None

class ReportReadWithOrganizationAndPath(ReportRead):
    path: Optional["PathRead"] = None
    organization: Optional["OrganizationRead"] = None

class ReportUpdate(SQLModel):
    infection_type: Optional[int] = None
    organization_id: Optional[int] = None


from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy_utc import UtcDateTime
from sqlmodel import Column, SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization, OrganizationRead
    from path import Path, PathRead, PathCreate, PathReadWithPoints
    from infection import Infection


class ReportBase(SQLModel):
    mask_worn: bool = Field(index=True, default=False, nullable=False)
    created: datetime = Field(sa_column=Column(UtcDateTime(timezone=True), nullable=False, index=True), index=True)

    organization_id: Optional[int] = Field(index=True, default=None, foreign_key="organization.id")
    infection_id: Optional[int] = Field(index=True, default=None, foreign_key="infection.id")


class Report(ReportBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(sa_relationship=RelationshipProperty("Organization", back_populates="reports", uselist=False))
    path: Optional["Path"] = Relationship(sa_relationship=RelationshipProperty("Path", back_populates="report", uselist=False))
    infection: Optional["Infection"] = Relationship(sa_relationship=RelationshipProperty("Infection", back_populates="reports", uselist=False))


# CRUD


class ReportCreate(ReportBase):
    path: Optional["PathCreate"] = None


class ReportRead(ReportBase):
    id: int


class ReportReadWithPath(ReportRead):
    path: Optional["PathRead"] = None


class ReportReadWithPathAndPoints(ReportRead):
    path: Optional["PathReadWithPoints"] = None


class ReportReadWithOrganization(ReportRead):
    organization: Optional["OrganizationRead"] = None


class ReportReadWithOrganizationAndPath(ReportRead):
    path: Optional["PathRead"] = None
    organization: Optional["OrganizationRead"] = None


class ReportUpdate(SQLModel):
    mask_worn: Optional[bool] = None
    organization_id: Optional[int] = None


from models.path import PathCreate, PathRead, PathReadWithPoints
ReportCreate.update_forward_refs()
ReportReadWithPath.update_forward_refs()
ReportReadWithPathAndPoints.update_forward_refs()
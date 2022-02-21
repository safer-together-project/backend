from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy_utc import UtcDateTime
from sqlmodel import Column, SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization, OrganizationRead
    from path import Path, PathRead, PathCreate, PathReadWithPoints
    from infection_condition import InfectionCondition, InfectionConditionRead, InfectionConditionReadWithInfection


class ReportBase(SQLModel):
    created: datetime = Field(sa_column=Column(UtcDateTime(timezone=True), nullable=False, index=True), index=True)

    organization_id: Optional[int] = Field(index=True, default=None, foreign_key="organization.id")
    infection_condition_id: Optional[int] = Field(index=True, default=None, foreign_key="infectioncondition.id")


class Report(ReportBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(sa_relationship=RelationshipProperty("Organization", back_populates="reports", uselist=False))
    path: Optional["Path"] = Relationship(sa_relationship=RelationshipProperty("Path", back_populates="report", uselist=False))
    infection_condition: Optional["InfectionCondition"] = Relationship(sa_relationship=RelationshipProperty("InfectionCondition", back_populates="reports", uselist=False))


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

class ReportReadWithInfectionInfoAndPathAndPoints(ReportRead):
    path: Optional["PathReadWithPoints"] = None
    infection_condition: Optional["InfectionConditionReadWithInfection"] = None

class ReportUpdate(SQLModel):
    organization_id: Optional[int] = None
    infection_condition_id: Optional[int] = None


from models.path import PathCreate, PathRead, PathReadWithPoints
from models.infection_condition import InfectionConditionReadWithInfection
ReportCreate.update_forward_refs()
ReportReadWithPath.update_forward_refs()
ReportReadWithPathAndPoints.update_forward_refs()
ReportReadWithInfectionInfoAndPathAndPoints.update_forward_refs()
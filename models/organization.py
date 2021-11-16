from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from beacon import Beacon, BeaconRead
    from report import Report, ReportRead
    from employee import Employee, EmployeeRead

class OrganizationBase(SQLModel):
    name: str = Field(max_length=256)
    access_code: str = Field(sa_column_kwargs={"unique": True}, max_length=6, nullable=False)

class Organization(OrganizationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    beacons: List["Beacon"] = Relationship(back_populates="organization")
    reports: List["Report"] = Relationship(back_populates="organization")
    employees: List["Employee"] = Relationship(back_populates="organization")

# CRUD

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationRead(OrganizationBase):
    id: int

class OrganizationReadWithBeacons(OrganizationRead):
    beacons: List["BeaconRead"] = []

class OrganizationReadWithReports(OrganizationRead):
    reports: List["ReportRead"] = []

class OrganizationReadWithEmployees(OrganizationRead):
    employees: List["EmployeeRead"] = []

class OrganizationReadWithReporsAndBeacons(OrganizationRead):
    beacons: List["BeaconRead"] = []
    reports: List["ReportRead"] = []

class OrganizationUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    access_code: Optional[str] = None
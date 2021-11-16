from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from organization import Organization, OrganizationRead

class EmployeeBase(SQLModel):
    first_name: str = Field(max_length=256)
    last_name: str = Field(max_length=256)
    username: str = Field(max_length=256)
    password: str = Field(max_length=256)

    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")

class Employee(EmployeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    organization: Optional["Organization"] = Relationship(back_populates="employees")

# CRUD

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeRead(EmployeeBase):
    id: int

class EmployeeReadWithOrganization(EmployeeRead):
    organization: Optional["OrganizationRead"] = None

class EmployeeUpdate(SQLModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
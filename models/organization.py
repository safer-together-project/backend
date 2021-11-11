from typing import List, Optional, TYPE_CHECKING
from sqlalchemy.sql.schema import Column
from sqlmodel import SQLModel, Field, Relationship, String

if TYPE_CHECKING:
    from beacon import Beacon
    from report import Report

class OrganizationBase(SQLModel):
    name: str = Field(max_length=256)
    access_code: str = Field(sa_column_kwargs={"unique": True}, max_length=6, nullable=False)

class Organization(OrganizationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    beacons: List["Beacon"] = Relationship(back_populates="organization")
    reports: List["Report"] = Relationship(back_populates="organization")

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationRead(OrganizationBase):
    id: int

class OrganizationUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    access_code: Optional[str] = None
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy.sql.schema import Column
from sqlmodel import SQLModel, Field, Relationship, String

if TYPE_CHECKING:
    from beacon import Beacon
    from report import Report

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(max_length=256)
    access_code: str = Field(sa_column=(Column("access_code", String, unique=True)), max_length=6, nullable=False)

    beacons: List["Beacon"] = Relationship(back_populates="organization")
    reports: List["Report"] = Relationship(back_populates="organization")
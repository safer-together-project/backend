from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from beacon import Beacon
    from report import Report

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    access_code: str

    beacons: List["Beacon"] = Relationship(back_populates="organization")
    reports: List["Report"] = Relationship(back_populates="organization")
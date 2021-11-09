from typing import List, Optional
from sqlmodel import SQLModel, Field
from sqlmodel.main import Relationship

from models.beacon import Beacon
from models.report import Report


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    access_code: str

    beacons: List["Beacon"] = Relationship(back_populates="organization")
    reports: List["Report"] = Relationship(back_populates="organization")
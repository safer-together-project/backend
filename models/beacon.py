from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

from models.organization import Organization


class Beacon(SQLModel, table=True):
    id: str = Field(primar_key=True)
    organization_id: Optional[int] = Field(default=None, foreign_key="Organization.id")
    major: int
    minor: int
    status: int
    longitude: float
    latitude: float

    organization: Optional[Organization] = Relationship(back_populates="beacons")
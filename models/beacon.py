from typing import Optional, TYPE_CHECKING
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization

class BeaconBase(SQLModel):
    status: int
    longitude: float
    latitude: float

    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")

class Beacon(BeaconBase, table=True):
    id: str = Field(primary_key=True, max_length=35)
    major: int = Field(primary_key=True)
    minor: int = Field(primary_key=True)

    organization: Optional["Organization"] = Relationship(back_populates="beacons")

class BeaconCreate(BeaconBase):
    pass

class BeaconRead(BeaconBase):
    id: str
    major: int
    minor: int

class BeaconUpdate(SQLModel):
    status: Optional[int] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    organization_id: Optional[int] = None
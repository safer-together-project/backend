from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from organization import Organization

class Beacon(SQLModel, table=True):
    id: str = Field(primary_key=True, index=True, max_length=35)
    organization_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    major: int
    minor: int
    status: int
    longitude: float
    latitude: float

    organization: Optional["Organization"] = Relationship(back_populates="beacons")
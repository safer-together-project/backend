from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

from models.organization import Organization
from models.path import Path


class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(default=None, foreign_key="Organization.id")
    infection_type: int

    organization: Optional[Organization] = Relationship(back_populates="reports")
    path: Optional[Path] = Relationship(back_populates="report")
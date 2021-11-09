from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from models.point import Point

from models.report import Report


class Path(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: Optional[int] = Field(default=None, foreign_key="Report.id")

    report: Optional[Report] = Relationship(back_populates="path")
    points: List["Point"] = Relationship(back_populates="path")
from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from report import Report
    from point import Point

class PathBase(SQLModel):
    report_id: Optional[int] = Field(default=None, foreign_key="report.id")

class Path(PathBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    report: Optional["Report"] = Relationship(back_populates="path")
    points: List["Point"] = Relationship(back_populates="path")

class PathCreate(PathBase):
    pass

class PathRead(PathBase):
    id: int

class PathUpdate(SQLModel):
    id: Optional[int] = None
    report_id: Optional[int] = None
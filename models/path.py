from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from report import Report
    from point import Point

class Path(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    report_id: Optional[int] = Field(default=None, foreign_key="report.id")

    report: Optional["Report"] = Relationship(back_populates="path")
    points: List["Point"] = Relationship(back_populates="path")
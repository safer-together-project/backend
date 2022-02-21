from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column
from sqlalchemy_utc import UtcDateTime
from sqlmodel import SQLModel, Field, Relationship, Column
from pydantic.json import isoformat

if TYPE_CHECKING:
    from report import Report, ReportRead
    from point import Point, PointRead, PointCreate


class PathBase(SQLModel):
    date: datetime = Field(sa_column=Column(UtcDateTime(timezone=True), nullable=False, index=True), index=True)

    report_id: Optional[int] = Field(index=True, default=None, foreign_key="report.id")


class Path(PathBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    report: Optional["Report"] = Relationship(back_populates="path")
    points: List["Point"] = Relationship(back_populates="path")

    class Config:
        json_encoders = {
            datetime: isoformat
        }


class PathCreate(PathBase):
    points: List["PointCreate"] = []


class PathRead(PathBase):
    id: int


class PathReadWithReport(PathRead):
    report: Optional["ReportRead"] = None


class PathReadWithPoints(PathRead):
    points: List["PointRead"] = []


class PathReadWithReportAndPoints(PathRead):
    report: Optional["ReportRead"] = None
    points: List["PointRead"] = []


class PathUpdate(SQLModel):
    id: Optional[int] = None
    report_id: Optional[int] = None


from models.point import PointCreate, PointRead
PathCreate.update_forward_refs()
PathReadWithPoints.update_forward_refs()
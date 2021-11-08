from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer
from core.database import Base
from sqlalchemy import Column


class Path(Base):
    __tablename__ = 'Path'

    id = Column(Integer, primary_key=true, autoincrement=true)
    report_id = Column(Integer, ForeignKey("Report.id"))

    report = relationship("Report", back_populates="path")
    path = relationship("Point", back_populates="path")
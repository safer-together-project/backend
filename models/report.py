from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer
from core.database import Base
from sqlalchemy import Column


class Report(Base):
    __tablename__ = 'Report'

    id = Column(Integer, primary_key=true, autoincrement=true)
    organization_id = Column(Integer, ForeignKey("Organization.id"))
    infection_type = Column(Integer)

    organization = relationship("Organization", back_populates="report")

    path = relationship("Path", back_populates="report")
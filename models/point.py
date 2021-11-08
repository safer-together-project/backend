from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime, Float, Integer
from core.database import Base
from sqlalchemy import Column


class Point(Base):
    __tablename__ = 'Point'

    id = Column(Integer, primary_key=true, autoincrement=true)
    beacon_id = Column(Integer, ForeignKey("Beacon.id"))
    path_id = Column(Integer, ForeignKey("Path.id"))
    initial_timestamp = Column(DateTime)
    final_timestamp = Column(DateTime)
    longitude = Column(Float)
    latitude = Column(Float)

    # ORM Models
    beacon = relationship("Beacon")
    path = relationship("Path", back_populates="points")
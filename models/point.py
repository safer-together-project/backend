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
    coordinates_id = Column(Integer, ForeignKey("Coordinates.id"))
    path_id = Column(Integer, ForeignKey("Path.id"))
    initial_timestamp = Column(DateTime)
    final_timestamp = Column(DateTime)

    # ORM Models
    beacon = relationship("Beacon")
    coordinates = relationship("Coordinates")
    path = relationship("Path", back_populates="point")
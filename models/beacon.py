from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import ARRAY, Float, Integer
from config.database import Base
from sqlalchemy import Column, String

from models.coordinates import Coordinates


class Beacon(Base):
    __tablename__ = 'Beacon'

    id = Column(String, primary_key=true)
    organization_id = Column(String, ForeignKey('Organization.id'))
    location_id = Column(String, ForeignKey('Coordinates.id'))
    major = Column(Integer)
    minor = Column(Integer)
    status = Column(Integer)
    organization = relationship("Organization", back_populates="beacons")
    coordinates = relationship("Coordinates")
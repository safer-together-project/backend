from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from core.database import Base
from sqlalchemy import Column, String


class Beacon(Base):
    __tablename__ = 'Beacon'

    id = Column(String, primary_key=true)
    organization_id = Column(Integer, ForeignKey('Organization.id'))
    coordinates_id = Column(Integer, ForeignKey('Coordinates.id'))
    major = Column(Integer)
    minor = Column(Integer)
    status = Column(Integer)

    ## ORM Values
    organization = relationship("Organization", back_populates="beacons")
    coordinates = relationship("Coordinates")
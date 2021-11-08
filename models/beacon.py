from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer
from core.database import Base
from sqlalchemy import Column, String


class Beacon(Base):
    __tablename__ = 'Beacon'

    id = Column(String, primary_key=true)
    organization_id = Column(Integer, ForeignKey('Organization.id'))
    major = Column(Integer)
    minor = Column(Integer)
    status = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)

    ## ORM Values
    organization = relationship("Organization", back_populates="beacons")

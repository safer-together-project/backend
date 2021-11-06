from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from config.database import Base
from sqlalchemy import Column, String


class Organization(Base):
    __tablename__ = 'Organization'

    id = Column(String, primary_key=true, index=true)
    name = Column(String)
    access_code = Column(String)
    beacons = relationship(
        "Beacon",
        cascade="all,delete-orphan",
        back_populates="organization",
        uselist=True
    )
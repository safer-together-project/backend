from core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import Integer


class Organization(Base):
    __tablename__ = 'Organization'

    id = Column(Integer, primary_key=true, autoincrement=true)
    name = Column(String)
    access_code = Column(String)

    reports = relationship("Report", 
                back_populates="organization", 
                uselist=True
    )

    beacons = relationship(
        "Beacon",
        back_populates="organization",
        uselist=True
    )
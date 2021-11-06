from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Float
from config.database import Base
from sqlalchemy import Column, String


class Coordinates(Base):
    __tablename__ = 'Coordinates'

    id = Column(String, primary_key=true, index=true)
    longitude = Column(Float)
    latitude = Column(Float)

from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Float, Integer
from core.database import Base
from sqlalchemy import Column


class Coordinates(Base):
    __tablename__ = 'Coordinates'

    id = Column(Integer, primary_key=true, autoincrement=true)
    longitude = Column(Float)
    latitude = Column(Float)
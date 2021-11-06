import os

from sqlalchemy import create_engine
from typing import Generator

from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


username = os.environ.get("DB_USER")
password = os.environ.get("DB_SECRET")
host = os.environ.get("DB_HOST")
database_name = os.environ.get("DB_NAME")


Base = declarative_base()

DATABASE_URL = f'mariadb+mariadbconnector://{username}:{password}@{host}:3306/{database_name}'

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
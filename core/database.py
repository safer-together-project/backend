from sqlmodel import create_engine, Session
from typing import Generator

from sqlalchemy.orm import sessionmaker
from sqlmodel.main import SQLModel

from core.config import config


engine = create_engine(
    config.DB_URL,
    echo=config.DEBUG
)

SessionLocal = Session(engine)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLModel.metadata.create_all(engine)

def get_session() -> Generator:
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

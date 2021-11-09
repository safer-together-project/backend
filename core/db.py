import os
from sqlmodel import create_engine, Session
from sqlmodel.main import SQLModel
from core.config import config

engine = create_engine(config.DB_URL, echo=config.DEBUG)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def override_get_db():
    with Session(engine) as session:
        yield session

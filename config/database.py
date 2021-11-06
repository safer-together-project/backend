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

engine = create_engine(  # 2
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # 4

def get_db() -> Generator:
    db = SessionLocal()  # 2
    try:
        yield db  # 3
    finally:
        db.close()  # 4

# engine = create_async_engine(DATABASE_URL)

# SessionLocal = scoped_session(
#     sessionmaker(
#         autocommit=False,
#         autoflush=False,
#         bind=engine
#     )
# )


# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine,
#         class_=AsyncSession,
#         expire_on_commit=False,
#         autocommit=False,
#         autoflush=False
#     )

#     async with async_session() as session:
#         yield session


from fastapi import Depends, HTTPException, status
from datetime import timedelta, datetime

from typing import Optional

from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import user
from core.config import config
from core.db import get_session

from models.employee import Employee, EmployeeRead
from models.token import TokenData


SECRET_KEY = config.HASH_SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_employee(session: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    statement = select(Employee).where(Employee.username == token_data.username)
    result = await session.execute(statement)
    employee = result.scalar_one_or_none()
    if employee is None:
        raise credentials_exception
    return employee

async def authenticate_employee(username: str, password: str, session: AsyncSession) -> Optional[EmployeeRead]:
    statement = select(Employee).where(Employee.username == username)
    result = await session.execute(statement)

    employee = result.scalar_one_or_none()
    if not employee:
        return False
    if not verify_password(password, employee.password):
        return False
    return employee
from datetime import timedelta
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.token import Token
from utils.pwd_validation import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_employee, create_access_token

router = APIRouter(
    prefix="/organization",
    responses={404: {"description": "Not found"}},
    tags=["login"]
)
    
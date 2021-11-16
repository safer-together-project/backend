from datetime import timedelta
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.token import Token
from utils.pwd_validation import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_employee, create_access_token

router = APIRouter(
    prefix="/login",
    responses={404: {"description": "Not found"}},
    tags=["login"]
)

@router.post('', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    employee = await authenticate_employee(username=form_data.username, password=form_data.password, session=session)  # 2

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": employee.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
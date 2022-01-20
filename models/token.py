from typing import Optional
from pydantic import Field
from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str = Field(index=True)
    token_type: str = Field(index=True)


class TokenData(SQLModel):
    username: Optional[str] = None
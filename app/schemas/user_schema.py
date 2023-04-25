from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email : EmailStr = Field(..., description="user email")
    role: int
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str = Field(...,min_length=8, max_length=24, description="user password")
    first_name: str = Field(...,min_length=2, max_length=55, description="user first_name")
    last_name: str = Field(...,min_length=2, max_length=55, description="user last_name")
    mobile: str = Field(...,min_length=10, max_length=13, description="user mobile")
    adresse: str = Field(...,min_length=5, max_length=100, description="user adresse")
    cin: str = Field(...,min_length=12, max_length=12, description="user cin")

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(..., title='Title', max_length=55, min_length=2)
    last_name: Optional[str] = Field(..., title='Title', max_length=55, min_length=2)
    mobile: Optional[str] = Field(..., title='Title', max_length=13, min_length=10)
    adresse: Optional[str] = Field(..., title='Title', max_length=100, min_length=4)
    cin: Optional[str] = Field(..., title='Title', max_length=12, min_length=12)

class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    role: int
    first_name: str
    last_name: str
    mobile: str
    adresse: str
    cin: str
    disabled: Optional[bool]

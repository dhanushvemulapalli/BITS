from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from .base import BaseSchema
from ..models.user import UserRole
from datetime import date

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone_number: str
    role: Optional[UserRole] = UserRole.CUSTOMER

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[constr(min_length=2, max_length=100)] = None
    phone_number: Optional[str] = None
    password: Optional[constr(min_length=8)] = None

class UserInDB(UserBase, BaseSchema):
    is_verified: bool

class User(UserInDB):
    pass

class UserWithToken(User):
    access_token: str
    token_type: str = "bearer"

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 
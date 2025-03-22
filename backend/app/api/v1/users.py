from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.user import UserCreate, UserResponse
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=List[UserResponse])
async def get_users():
    # TODO: Implement user listing
    return [] 
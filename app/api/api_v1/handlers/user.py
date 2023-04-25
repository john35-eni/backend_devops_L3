from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserAuth, UserOut, UserUpdate
from app.services.user_service import UserService
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
import pymongo
from typing import List

user_router = APIRouter()

@user_router.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
# fonction à determiner
@user_router.get('/me', summary="Get detail of currently logged in user", response_model=UserOut)
async def get_current_logged_user(current_user: User = Depends(get_current_user)):
    return await UserService.get_user_by_email(current_user.email)

@user_router.get('/{user_id}', summary="Get user by user.id", response_model=UserOut)
async def retrieve(user_id: UUID, current_user: User = Depends(get_current_user)):
    return await UserService.get_user_by_id(user_id)

# get all user
@user_router.get('/', summary="Get all  user ", response_model=List[UserOut])
async def list(current_user: User = Depends(get_current_user)):
    return await UserService.list_user()
# update user 
@user_router.put('/{user_id}', summary="Update user by user_id", response_model=UserOut)
async def update(user_id: UUID, data: UserUpdate, current_user: User= Depends(get_current_user)):
    return await UserService.update_user( user_id, data)

# delete user
@user_router.delete('/{user_id}', summary="Delete user by user_id")
async def delete(user_id: UUID, current_user: User = Depends(get_current_user)):
    await UserService.delete_user( user_id)
    return None

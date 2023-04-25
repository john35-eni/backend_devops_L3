from typing import Optional
from uuid import UUID
from typing import List
from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.schemas.user_schema import UserUpdate
from app.core.security import get_password, verify_password

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username = user.username,
            email= user.email,
            role= user.role,
            hashed_password=get_password(user.password),
            mobile= user.mobile,
            adresse= user.adresse,
            cin= user.cin,
            first_name=user.first_name,
            last_name= user.last_name
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user 

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user  

    @staticmethod
    async def list_user() -> List[User]:
        user = await User.find_all().to_list()
        return user 

    @staticmethod
    async def retrieve_user(user_id: UUID):
        user = await User.find_one(User.user_id == user_id)
        return user 

    @staticmethod
    async def update_user( user_id: UUID, data: UserUpdate):
        user = await UserService.retrieve_user(user_id)
        await user.update({"$set" : data.dict(exclude_unset=True)})

        await user.save()
        return user

    @staticmethod
    async def delete_user(user_id: UUID):
        user = await UserService.retrieve_user(user_id)
        if user:
            await user.delete()
        return None  
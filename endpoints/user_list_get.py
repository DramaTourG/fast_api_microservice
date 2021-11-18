from typing import List
from fastapi import APIRouter, Depends
from repositories.users_repo import UserRepo
from .depends import get_user_repository
from models.user import UserOut

router = APIRouter()


@router.get('/user-list', response_model=List[UserOut])
async def read_users(users: UserRepo = Depends(get_user_repository)):
    return await users.get_all()

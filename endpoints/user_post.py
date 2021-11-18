from fastapi import APIRouter, Depends
from repositories.users_repo import UserRepo
from .depends import get_user_repository
from models.user_models import UserOut, UserIn

router = APIRouter()


@router.post("/user", response_model=UserOut, status_code=201)
async def create_user(user: UserIn, users: UserRepo = Depends(get_user_repository)):
    return await users.create(user)

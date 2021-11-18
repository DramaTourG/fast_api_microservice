from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository
from models.user_models import UserOut, UserIn
from repositories.users_repo import UserRepo

router = APIRouter()


@router.put("/user/{user_id}", response_model=UserOut)
async def update_user(user_id, u: UserIn, users: UserRepo = Depends(get_user_repository)):
    return await users.update_all(user_id=int(user_id), user=u)

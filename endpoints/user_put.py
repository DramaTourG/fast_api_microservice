from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository, get_user_from_token, verify_user
from models.user_models import UserOut, UserIn
from repositories.users_repo import UserRepo

router = APIRouter(dependencies=[Depends(get_user_from_token)])


@router.put("/user/{user_id}", response_model=UserOut)
async def update_user(user_id: int, u: UserIn,
                      users: UserRepo = Depends(get_user_repository),
                      verification: bool = Depends(verify_user)):
    if verification:
        return await users.update_all(user_id=user_id, user=u)

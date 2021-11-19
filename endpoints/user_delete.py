from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository, get_user_from_token, verify_user
from repositories.users_repo import UserRepo

router = APIRouter(dependencies=[Depends(get_user_from_token)])


@router.delete("/user/{user_id}")
async def delete_user(user_id: int,
                      users: UserRepo = Depends(get_user_repository),
                      verification: bool = Depends(verify_user)):
    if verification:
        return await users.delete(user_id=user_id)

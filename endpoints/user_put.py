from fastapi import APIRouter, Depends, HTTPException, status

from endpoints.depends import get_user_repository, get_current_user
from models.user_models import UserOut, UserIn
from repositories.users_repo import UserRepo

router = APIRouter()


@router.put("/user/{user_id}", response_model=UserOut)
async def update_user(user_id, u: UserIn,
                      users: UserRepo = Depends(get_user_repository),
                      current_user: UserIn = Depends(get_current_user)):
    user = await users.get_by_id(user_id=int(user_id))
    if user is None or user.email != current_user.email:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return await users.update_all(user_id=int(user_id), user=u)

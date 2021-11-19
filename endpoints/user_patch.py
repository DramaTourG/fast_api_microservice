from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository, get_user_from_token, verify_user
from models.user_models import UserFields
from repositories.users_repo import UserRepo

router = APIRouter(dependencies=[Depends(get_user_from_token)])


@router.patch("/user/{user_id}", response_model=UserFields, response_model_exclude={'password'})
async def update_user_fields(user_id: int, fields: UserFields,
                             users: UserRepo = Depends(get_user_repository),
                             verification: bool = Depends(verify_user)):
    if verification:
        return await users.update_required_fields(user_id=user_id, fields=fields)

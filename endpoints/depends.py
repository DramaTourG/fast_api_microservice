from fastapi import Depends, HTTPException, status

from models.user_models import UserIn
from repositories.users_repo import UserRepo
from db.base import database
from core.security import JWTBearer, decode_access_token


def get_user_repository() -> UserRepo:
    return UserRepo(database)


async def get_current_user(
        users: UserRepo = Depends(get_user_repository()),
        token: str = Depends(JWTBearer)) -> UserIn:
    credentials_exc = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exc
    email = payload.get("sub")
    if email is None:
        raise credentials_exc
    user = await users.get_by_email(email)
    if user is None:
        raise credentials_exc
    return user

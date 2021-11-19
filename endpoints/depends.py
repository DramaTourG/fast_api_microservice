from fastapi import Depends, HTTPException, status

from models.user_models import UserIn
from repositories.users_repo import UserRepo
from db.base import database
from core.security import JWTBearer, decode_access_token


def get_user_repository() -> UserRepo:
    return UserRepo(database)


async def get_user_from_token(
        users: UserRepo = Depends(get_user_repository),
        token: str = Depends(JWTBearer())) -> UserIn:
    credentials_exc = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
    credentials_exc1 = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials1')
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exc
    email = payload.get("sub")
    if email is None:
        raise credentials_exc1
    user = await users.get_by_email(email)
    if user is None:
        raise credentials_exc
    return user


async def verify_user(
        user_id: int,
        users: UserRepo = Depends(get_user_repository),
        token_user: UserIn = Depends(get_user_from_token)
) -> bool:
    user = await users.get_by_id(user_id=int(user_id))
    if user is None or user.email != token_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return True

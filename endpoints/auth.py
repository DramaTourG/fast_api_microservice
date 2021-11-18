from fastapi import APIRouter, Depends, HTTPException, status

from core.security import verify_password, create_access_token
from endpoints.depends import get_user_repository
from models.token_models import Token, Login
from repositories.users_repo import UserRepo

router = APIRouter()


@router.post("/login", response_model=Token, status_code=201)
async def login(credentials: Login, users: UserRepo = Depends(get_user_repository)):
    user = await users.get_by_email(credentials.email)
    if user is None or not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect credentials")
    return Token(access_token=create_access_token({"sub": user.email}),
                 token_type="Bearer")

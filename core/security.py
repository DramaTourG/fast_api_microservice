from datetime import datetime, timedelta
import bcrypt
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt


from core.config import ACCESS_TOKEN_EXPIRE_HOURS, SECRET_KEY, ALGORITHM


def verify_password(decoded_psw: str, psw_from_db: str) -> bool:
    return bcrypt.checkpw(decoded_psw.encode(), psw_from_db.encode())


def password_hashing(password: str) -> str:
    hashed_psw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return hashed_psw


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)


def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return decoded_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials and decode_access_token(credentials.credentials):
            return credentials.credentials
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

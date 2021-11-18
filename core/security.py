from datetime import datetime, timedelta

import bcrypt
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

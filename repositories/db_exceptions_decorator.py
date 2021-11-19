from fastapi import HTTPException, status
from functools import wraps


def db_error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            res = await func(*args, **kwargs)
            return res
        except Exception:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad request')
    return wrapper

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, constr


class UserOut(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    register_date: Optional[datetime] = None


class UserIn(BaseModel):
    username: constr(min_length=1, max_length=40)
    email: EmailStr
    password: constr(min_length=8, max_length=100)

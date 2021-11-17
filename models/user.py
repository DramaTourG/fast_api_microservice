from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr


class UserOut(BaseModel):
    id: Optional[str] = None
    username: str
    email: EmailStr
    register_date: datetime


class UserIn(BaseModel):
    username: constr(min_length=1, max_length=40)
    email: EmailStr
    password: constr(min_length=8, max_length=40)

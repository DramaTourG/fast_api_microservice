from datetime import datetime
from typing import List

from sqlalchemy import select

from core.security import password_hashing
from db.users import Users
from models.user_models import UserIn, UserOut
from .base import BaseRepo


class UsersException(Exception):
    pass


class UserRepo(BaseRepo):
    """CRUD"""
    async def create(self, user: UserIn):
        values = dict(**user.dict())
        values['password'] = password_hashing(values['password'])
        values['register_date'] = datetime.utcnow()
        query = Users.insert()
        values['id'] = await self.database.execute(query=query, values=values)
        return values

    async def get_all(self) -> List[UserOut]:
        users = select(Users)
        return await self.database.fetch_all(users)

    async def get_by_id(self, user_id: int) -> UserOut:
        user_query = select(Users).filter_by(id=user_id)
        user = await self.database.fetch_one(user_query)
        if user is not None:
            return UserOut.parse_obj(user)

    async def get_by_email(self, email: str) -> UserIn:
        user_query = select(Users).filter_by(email=email)
        user = await self.database.fetch_one(user_query)
        if user is not None:
            return UserIn.parse_obj(user)

    async def update_all(self, user_id: int, user: UserIn):
        values = dict(**user.dict())
        values['password'] = password_hashing(values['password'])
        query = Users.update().filter_by(id=user_id)
        await self.database.execute(query=query, values=values)
        values['id'] = user_id
        return values

    async def update_password(self):
        return

    async def delete(self, user_id):
        return

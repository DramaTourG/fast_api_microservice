from db.users import Users
from .base import BaseRepo


class UsersException(Exception):
    pass


class UserRepo(BaseRepo):

    async def get_all(self, limit: int = 100, skip: int = 0):
        return

    async def get_by_id(self, user_id: int):
        return

    async def update(self):
        return

    async def get_by_email(self, email: str):
        return

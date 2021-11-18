from repositories.users_repo import UserRepo
from db.base import database


def get_user_repository() -> UserRepo:
    return UserRepo(database)

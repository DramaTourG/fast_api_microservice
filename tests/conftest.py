import pytest
from databases import Database
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from core.security import create_access_token
from main import app
from models.user_models import UserOut, UserIn
from repositories.users_repo import UserRepo


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_database():
    from db.base import metadata
    engine = create_engine('sqlite:///db/test_db.sqlite')
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)
    database = Database('sqlite:///db/test_db.sqlite', force_rollback=True)
    yield database


@pytest.fixture()
def header(monkeypatch):
    user = {"id": 1,
            "username": "string",
            "email": "user@example.com",
            "password": "$stringst"}
    token = create_access_token({"sub": user["email"]})

    async def mock_get_by_email(*args, **kwargs):
        return UserIn.parse_obj(user)

    monkeypatch.setattr(UserRepo, "get_by_email", mock_get_by_email)

    async def mock_get_by_id(*args, **kwargs):
        return UserOut.parse_obj(user)

    monkeypatch.setattr(UserRepo, "get_by_id", mock_get_by_id)

    yield {"Authorization": "Bearer " + token}

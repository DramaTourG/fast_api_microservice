import json

from core.security import password_hashing
from models.user_models import UserIn
from repositories.users_repo import UserRepo


def test_login_post(test_app, monkeypatch):
    test_request_user = {"email": "user@example.com", "password": "stringst"}
    test_response_user = UserIn(username="TestUser", email="TESTuser@example.com",
                                password=password_hashing("stringst"))

    async def mock_post(*args, **kwargs):
        return test_response_user

    monkeypatch.setattr(UserRepo, "get_by_email", mock_post)

    response = test_app.post("/login", data=json.dumps(test_request_user),)

    assert response.status_code == 201
    assert len(response.json()["access_token"]) == 144
    assert response.json()["token_type"] == 'Bearer'


def test_user_post_invalid_json(test_app):
    response = test_app.post("/login", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

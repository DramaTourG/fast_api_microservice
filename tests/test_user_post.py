import json
from datetime import datetime

from repositories.users_repo import UserRepo


def test_user_post(test_app, monkeypatch):
    test_request_user = {"username": "string", "email": "user@example.com", "password": "stringst"}
    test_response_user = {"id": 1, "username": "string", "email": "user@example.com",
                          "register_date": datetime.utcnow().isoformat()}

    async def mock_post(*args, **kwargs):
        return test_response_user

    monkeypatch.setattr(UserRepo, "create", mock_post)

    response = test_app.post("/user", data=json.dumps(test_request_user),)

    assert response.status_code == 201
    assert response.json() == test_response_user


def test_user_post_invalid_json(test_app):
    response = test_app.post("/user", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

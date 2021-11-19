import json

from models.user_models import UserFields
from repositories.users_repo import UserRepo

test_user = {"id": 1,
             "username": "string",
             "email": "user@example.com",
             "password": "$stringst"}


def test_user_patch_invalid_json(test_app, monkeypatch, header):
    response = test_app.patch("/user/1", headers=header(test_user, monkeypatch),
                              data=json.dumps({"email": "string"}))
    assert response.status_code == 422


def test_user_patch(test_app, monkeypatch, header):
    request_fields = {"username": "TestUser5"}
    response_fields = UserFields(username="TestUser5", id=1)

    async def mock_patch(*args, **kwargs):
        return response_fields

    monkeypatch.setattr(UserRepo, "update_required_fields", mock_patch)

    response = test_app.patch("/user/1", headers=header(test_user, monkeypatch),
                              data=json.dumps(request_fields))

    assert response.status_code == 200
    assert response.json() == {'id': 1, 'username': 'TestUser5', 'email': None, 'password': None}

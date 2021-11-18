import json

from repositories.users_repo import UserRepo


def test_user_put(test_app, monkeypatch):
    test_request_user = {"username": "string", "email": "user@example.com", "password": "stringst"}
    test_response_user = {"id": 1,
                          "username": "string",
                          "email": "user@example.com",
                          "password": "$stringst"}

    async def mock_put(*args, **kwargs):
        return test_response_user

    monkeypatch.setattr(UserRepo, "update_all", mock_put)

    response = test_app.put("/user/1", data=json.dumps(test_request_user),)
    test_response_user['register_date'] = None
    del test_response_user['password']
    assert response.status_code == 200
    assert response.json() == test_response_user


def test_user_post_invalid_json(test_app):
    response = test_app.put("/user/1", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

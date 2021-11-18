from datetime import datetime

from repositories.users_repo import UserRepo


def test_user_list_get(test_app, monkeypatch):
    test_response_user_list = [
        {"id": 1, "username": "string", "email": "user@example.com",
         "register_date": datetime.utcnow(), "password": "54213542sffda"},
        {"id": 2, "username": "string2", "email": "user2@example.com",
         "register_date": datetime.utcnow(), "password": "12343542sffda"}]

    async def mock_post(*args, **kwargs):
        return test_response_user_list

    monkeypatch.setattr(UserRepo, "get_all", mock_post)

    response = test_app.get("/user-list")
    for user in test_response_user_list:
        del user["password"]
        user["register_date"] = user["register_date"].isoformat()

    assert response.status_code == 200
    assert response.json() == test_response_user_list

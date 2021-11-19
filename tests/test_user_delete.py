from repositories.users_repo import UserRepo


def test_user_patch(test_app, monkeypatch, header):

    async def mock_delete(*args, **kwargs):
        return 1

    monkeypatch.setattr(UserRepo, "delete", mock_delete)

    response = test_app.delete("/user/1", headers=header)

    assert response.status_code == 200
    assert response.json() == {'id': 1}

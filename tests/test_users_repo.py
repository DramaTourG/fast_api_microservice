import asyncio
from sqlite3 import IntegrityError

import pytest

from models.user_models import UserIn, UserOut
from repositories.users_repo import UserRepo


@pytest.fixture(scope="module")
def test_user_repo(test_database):
    user_repo = UserRepo(test_database)
    yield user_repo


user1 = UserIn(username="TestUser", email="TESTuser@example.com", password="stringsthgk")
user2 = UserIn(username="TestUser2", email="TESTuser2@example.com", password="stringsthgk")
update_user = UserIn(username="TestUser3", email="TESTuser3@example.com", password="stringsthgk")


def test_create(test_user_repo):
    response1 = asyncio.run(test_user_repo.create(user1))
    response2 = asyncio.run(test_user_repo.create(user2))
    with pytest.raises(IntegrityError):
        asyncio.run(test_user_repo.create(user1))
    assert response1['id'] == 1
    assert response1['email'] == "TESTuser@example.com"
    assert response1['username'] == "TestUser"
    assert response2['id'] == 2
    assert response2['email'] == "TESTuser2@example.com"
    assert response2['username'] == "TestUser2"
    assert response1['register_date'] < response2['register_date']
    assert response1['password'] != response2['password']


def test_get_all(test_user_repo):
    res = asyncio.run(test_user_repo.get_all())
    assert type(res) == list
    assert len(res) == 2
    assert res[0]['username'] == "TestUser"
    assert res[1]['username'] == "TestUser2"


def test_get_by_id(test_user_repo):
    res = asyncio.run(test_user_repo.get_by_id(2))
    user = dict(**res.dict())
    assert type(res) == UserOut
    assert user['username'] == "TestUser2"


def test_update_all(test_user_repo):
    response = asyncio.run(test_user_repo.update_all(2, update_user))
    assert response['email'] == 'TESTuser3@example.com'
    assert response['username'] == 'TestUser3'
    assert response['id'] == 2


def test_get_by_email(test_user_repo):
    res = asyncio.run(test_user_repo.get_by_email('TESTuser3@example.com'))
    user = dict(**res.dict())
    assert type(res) == UserIn
    assert user['username'] == "TestUser3"

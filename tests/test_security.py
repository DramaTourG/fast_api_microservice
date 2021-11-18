import pytest

from core.security import verify_password, password_hashing, create_access_token, decode_access_token


def test_hashing_and_verify_psw():
    psw = "ExtremelySecret"
    hashed_password = password_hashing(psw)
    assert verify_password(psw, hashed_password)
    with pytest.raises(ValueError):
        verify_password(hashed_password, psw)
    assert verify_password('WrongPassword', hashed_password) is False


def test_create_access_token():
    data = {"sub": "test@email.com"}
    token = create_access_token(data)
    data2 = decode_access_token(token)

    assert type(token) == str
    assert data['sub'] == data2['sub']
    assert data2['exp']

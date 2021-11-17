import pytest

from core.security import verify_password, password_hashing


def test_hashing_and_verify_psw():
    psw = "ExtremelySecret"
    hashed_password = password_hashing(psw)
    assert verify_password(psw, hashed_password)
    with pytest.raises(ValueError):
        verify_password(hashed_password, psw)
    assert verify_password('WrongPassword', hashed_password) is False

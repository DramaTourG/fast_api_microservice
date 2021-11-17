import bcrypt


def verify_password(decoded_psw, psw_from_db):
    return bcrypt.checkpw(decoded_psw.encode(), psw_from_db.encode())


def password_hashing(password):
    hashed_psw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return hashed_psw

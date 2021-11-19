from starlette.config import Config

config = Config('.env')

DATABASE_URL = config(
    "DATABASE_URL", cast=str,
    default="postgresql://Dev:hello@localhost:5432/development_db")
ACCESS_TOKEN_EXPIRE_HOURS = 20
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="N0tASecretKey")
ORIGINS = config("SECRET_KEY", cast=list, default=["http://localhost", "http://localhost:8080"])

from starlette.config import Config

config = Config('.env')

DATABASE_URL = config(
    "EE_DATABASE_URL", cast=str,
    default="postgresql://Dev:hello@localhost:5432/development_db")

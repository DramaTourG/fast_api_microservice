import os
import dotenv

dotenv.load_dotenv('.env')

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://Dev:hello@localhost:5432/development_db")
ACCESS_TOKEN_EXPIRE_HOURS = 20
ALGORITHM = "HS256"
SECRET_KEY = os.environ.get("SECRET_KEY", "N0tASecretKey")
ORIGINS = os.environ.get("ORIGINS", ["http://localhost", "http://localhost:8080"])

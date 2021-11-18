import pytest
from databases import Database
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_database():
    from db.base import metadata
    engine = create_engine('sqlite:///db/test_db.sqlite')
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)
    database = Database('sqlite:///db/test_db.sqlite', force_rollback=True)
    yield database

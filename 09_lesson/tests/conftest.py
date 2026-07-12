import pytest

from src.database import Session


@pytest.fixture
def db_session():

    session = Session()

    yield session

    session.close()

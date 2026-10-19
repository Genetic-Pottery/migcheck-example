import pytest

import app


@pytest.fixture
def conn():
    """Runs each test in a transaction and rolls it back afterward."""
    with app.connect() as c:
        yield c
        c.rollback()

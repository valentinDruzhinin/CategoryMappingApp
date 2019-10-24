import pytest
from app import app
from app.models import Category


@pytest.yield_fixture(scope='session')
def client():
    with app.app_context():
        app.db.session.query(Category).delete()
        app.db.session.commit()
        yield app.test_client()
        app.db.session.query(Category).delete()
        app.db.session.commit()

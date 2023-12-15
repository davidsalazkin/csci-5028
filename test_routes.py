import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_fetch_articles(client):
    response = client.get('/fetch-articles').data
    assert len(response) > 0

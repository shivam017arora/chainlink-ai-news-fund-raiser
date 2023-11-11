import pytest
from serv import app as flask_app  # Assuming your Flask app is in a file named app.py

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_charity_endpoint_no_data(client):
    response = client.post('/api/charity')
    assert response.status_code == 415

def test_charity_endpoint_with_valid_data(client):
    valid_data = {'category': 'health'}
    response = client.post('/api/charity', json=valid_data)
    assert response.status_code == 201
    assert 'result' in response.json

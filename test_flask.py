# test_flask.py
import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_route(client):
    data = {'features': [5.1, 3.5, 1.4, 0.2]}
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert 'prediction' in response.json()

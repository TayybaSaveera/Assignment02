# test_flask.py
import pytest
from app import app  # Ensure this import reflects the structure of your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_route(client):
    data = [5.1, 3.5, 1.4, 0.2]  # Assuming your Flask endpoint expects this JSON structure
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert 'predicted_species' in response.get_json()  # Adjust the key based on your actual response structure

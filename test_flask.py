from app import app
import pytest
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    response = client.post('/predict', json={'features': {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2}})
    data = response.json
    assert response.status_code == 200
    assert 'predicted_species' in data

from fastapi.testclient import TestClient
import sys
sys.path.append("src/serving")
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_prediction():
    response = client.post("/predict", json={"price": 10.0, "competitor_price": 12.0, "day_of_week": 1})
    assert response.status_code == 200
    assert "predicted_demand" in response.json()

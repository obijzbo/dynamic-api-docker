from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_greetins():
    response = client.get("/greetins")
    assert response.status_code == 200
    assert "Hello" in response.text

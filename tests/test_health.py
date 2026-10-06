from fastapi.testclient import TestClient
from ai_business_assistant.main import app

client = TestClient(app)

def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "AI Business Assistant"
    assert data["status"] == "running"

def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
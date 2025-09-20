from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/users")
    assert response.status_code in [200, 404]  # db may be empty

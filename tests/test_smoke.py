# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_root_endpoint():
#     response = client.get("/users")
#     assert response.status_code in [200, 404]  # db may be empty
# tests/test_app_startup.py
from app.main import app

def test_app_exists():
    assert app is not None

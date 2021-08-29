from app.main import app
from starlette.testclient import TestClient


def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200

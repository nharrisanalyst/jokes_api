from starlette.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_base_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


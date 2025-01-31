from fastapi.testclient import TestClient

from app.database import Base
from main import app

client = TestClient(app)


def test_read_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello World", "Super": "gogo", "mama": "fatass very nice"}

import pytest
from backend.main import app
from fastapi.testclient import TestClient
from core.validators import StringInput, StringOutput
from backend.src.challenges.string_challenge import StringChallenge

client = TestClient(app)


def test_valid_strings():
    challenge = StringChallenge()
    assert challenge.execute(StringInput(text="BA")).is_valid is True
    assert challenge.execute(StringInput(text="BCA")).is_valid is True


def test_invalid_strings():
    challenge = StringChallenge()
    assert challenge.execute(StringInput(text="ABC")).is_valid is False
    assert challenge.execute(StringInput(text="BCD")).is_valid is False
    assert challenge.execute(StringInput(text="ba")).is_valid is False
    assert challenge.execute(StringInput(text="B")).is_valid is False
    assert challenge.execute(StringInput(text="A")).is_valid is False
    with pytest.raises(Exception):
        challenge.execute(StringInput(text=""))

    
def test_post_string_valid():
    response = client.post("/api/v1/string/", json={"text": "BA"})
    assert response.status_code == 200
    assert response.json()["is_valid"] is True


def test_post_string_invalid():
    response = client.post("/api/v1/string/", json={"text": "BCD"})
    assert response.status_code == 200
    assert response.json()["is_valid"] is False


def test_post_string_empty():
    response = client.post("/api/v1/string/", json={"text": ""})
    # Se o campo for obrigatório e não aceitar vazio, pode ser 422
    assert response.status_code in (200, 422)
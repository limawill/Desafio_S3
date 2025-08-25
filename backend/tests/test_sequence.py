import pytest
from backend.main import app
from fastapi.testclient import TestClient
from core.validators import SequenceInput, SequenceOutput
from backend.src.challenges.sequence_challenge import SequenceChallenge

client = TestClient(app)


def test_sequence_unit_valid():
    challenge = SequenceChallenge()
    result = challenge.execute(SequenceInput(position=5))
    assert isinstance(result, SequenceOutput)
    assert result.result == 39


def test_sequence_unit_invalid():
    challenge = SequenceChallenge()
    # Posição inválida (zero ou negativa)
    with pytest.raises(Exception):
        challenge.execute(SequenceInput(position=0))
    with pytest.raises(Exception):
        challenge.execute(SequenceInput(position=-1))


def test_post_sequence_valid():
    response = client.post("/api/v1/sequence/", json={"position": 6})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert data["result"] == 46


def test_post_sequence_invalid():
    response = client.post("/api/v1/sequence/", json={"position": 0})
    assert response.status_code == 422  # Pydantic validation error

    response = client.post("/api/v1/sequence/", json={"position": -3})
    assert response.status_code == 422  # Pydantic validation error


def test_post_sequence_missing_field():
    response = client.post("/api/v1/sequence/", json={})
    assert response.status_code == 422  # Campo obrigatório ausente
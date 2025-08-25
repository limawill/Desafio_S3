import pytest
from backend.main import app
from fastapi.testclient import TestClient
from core.validators import BoardGameInput, BoardGameOutput
from backend.src.challenges.board_game_challenge import BoardGameChallenge


client = TestClient(app)


def test_board_game_unit_valid():
    challenge = BoardGameChallenge()
    result = challenge.execute(BoardGameInput(board_size=3, board=[1, 2, 3]))
    assert isinstance(result, BoardGameOutput)
    assert hasattr(result, "turns")
    assert hasattr(result, "probability")
    assert hasattr(result, "combinations")
    assert result.turns == 1
    assert result.probability == 1.0
    assert result.combinations == 3


def test_board_game_unit_invalid():
    challenge = BoardGameChallenge()
    result = challenge.execute(BoardGameInput(board_size=5, board=[1, 2]))
    assert result.turns == 0 or result.probability == 0 or result.combinations == 0


def test_post_board_game_valid():
    response = client.post("/api/v1/board_game/", json={
        "board_size": 3,
        "board": [1, 2, 3]
    })
    assert response.status_code == 200
    data = response.json()
    assert "turns" in data
    assert "probability" in data
    assert "combinations" in data
    assert data["turns"] == 1
    assert data["probability"] == 1.0
    assert data["combinations"] == 3


def test_post_board_game_invalid():
    # board menor que board_size
    response = client.post("/api/v1/board_game/", json={
        "board_size": 5,
        "board": [1, 2]
    })
    # Pode ser 422 se o pydantic validar, ou 200 com erro na lógica
    assert response.status_code in (200, 422)


def test_post_board_game_missing_field():
    response = client.post("/api/v1/board_game/", json={})
    assert response.status_code == 422  # Campo obrigatório ausente
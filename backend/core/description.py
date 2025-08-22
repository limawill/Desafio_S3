# backend/core/description.py
from pydantic import BaseModel
from datetime import date

# Descrições e exemplos para cada rota
DESCRIPTIONS = {
    "string": {
        "description": "Validates if the input is a valid string starting with B and ending with A. The string must be longer than 1 character.",
        "example_input": {"text": "hello"},
        "response_model": BaseModel,
    },
    "sequence": {
        "description": "Calculates the value of a number sequence based on a position (greater than 0).",
        "example_input": {"position": 5},
        "response_model": BaseModel,
    },
    "board_game": {
        "description": "Solves a board game by calculating the minimum number of turns, success probability, and combinations without loops, given the board size and the list of jumps.",
        "example_input": {"board_size": 3, "board": [1, 1, 1]},
        "response_model": BaseModel,
    },
    "benefits": {
        "description": "Calculates the proportional value of vacation and thirteenth salary when resigning, based on salary and the dates of admission and resignation.",
        "example_input": {
            "salary": 3000.0,
            "hire_date": "2024-01-01",
            "resignation_date": "2025-08-21",
        },
        "response_model": BaseModel,
    },
}


# Modelos de exemplo para Swagger (opcional, para maior precisão)
class StringInputExample(BaseModel):
    text: str = "hello"


class SequenceInputExample(BaseModel):
    position: int = 5


class BoardGameInputExample(BaseModel):
    board_size: int = 3
    board: list[int] = [1, 1, 1]


class BenefitsInputExample(BaseModel):
    salary: float = 3000.0
    hire_date: date = date(2024, 1, 1)
    resignation_date: date = date(2025, 8, 21)

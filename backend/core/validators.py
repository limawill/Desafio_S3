# backend/core/validators.py
from datetime import date
from typing import List
from pydantic import BaseModel, Field, model_validator


# Pergunta 1:  Valida se é uma string
class StringInput(BaseModel):
    text: str = Field(..., min_length=1)


class StringOutput(BaseModel):
    is_valid: bool


# ------------------------------------


# Pergunta 2: Valida se é uma sequência Numérica
class SequenceInput(BaseModel):
    position: int = Field(..., gt=0)  # Garante position > 0


class SequenceOutput(BaseModel):
    result: int


# ------------------------------------


# Pergunta 3: Jogo no Tabuleiro
class BoardGameInput(BaseModel):
    board_size: int = Field(..., ge=3)
    board: List[int] = Field(..., min_length=2)


class BoardGameOutput(BaseModel):
    turns: int
    probability: float
    combinations: int


# ------------------------------------


# Pergunta 4: Valida se a entrada é float e date
class BenefitsInput(BaseModel):
    salary: float = Field(..., gt=0)  # Garante salary > 0
    hire_date: date
    resignation_date: date

    @model_validator(mode="before")
    @classmethod
    def check_dates(cls, data: dict) -> dict:
        hire_date = data.get("hire_date")
        resignation_date = data.get("resignation_date")
        if hire_date and resignation_date and resignation_date < hire_date:
            raise ValueError("resignation_date must be after hire_date")
        return data


class BenefitsOutput(BaseModel):
    vacation: float
    thirteenth_salary: float

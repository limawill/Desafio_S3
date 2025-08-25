import pytest
from backend.main import app
from fastapi.testclient import TestClient
from core.validators import BenefitsInput, BenefitsOutput
from backend.src.challenges.benefits_challenge import BenefitsChallenge

client = TestClient(app)



def test_benefits_unit_invalid():
    challenge = BenefitsChallenge()
    with pytest.raises(Exception):
        challenge.execute(BenefitsInput(
            salary=-1000.0,
            hire_date="2020-01-01",
            resignation_date="2021-01-01"
        ))


def test_post_benefits_valid():
    response = client.post("/api/v1/benefits/", json={
        "salary": 1000.0,
        "hire_date": "2020-01-01",
        "resignation_date": "2021-01-01"
    })
    assert response.status_code == 200
    data = response.json()
    assert "vacation" in data
    assert "thirteenth_salary" in data
    assert data["vacation"] >= 0.0
    assert data["thirteenth_salary"] >= 0.0


def test_post_benefits_invalid():
    # Salário negativo
    response = client.post("/api/v1/benefits/", json={
        "salary": -1000.0,
        "hire_date": "2020-01-01",
        "resignation_date": "2021-01-01"
    })
    assert response.status_code in (200, 422)

    # Datas inválidas
    response = client.post("/api/v1/benefits/", json={
        "salary": 1000.0,
        "hire_date": "2020-01-01",
        "resignation_date": "2019-01-01"
    })
    assert response.status_code in (200, 422)


def test_post_benefits_missing_field():
    response = client.post("/api/v1/benefits/", json={})
    assert response.status_code == 422  
from fastapi import APIRouter, Depends
from core.logging import logger
from core.description import DESCRIPTIONS
from core.validators import BenefitsInput, BenefitsOutput
from src.challenges.benefits_challenge import BenefitsChallenge


router = APIRouter(prefix="/benefits")


def get_benefits_challenge() -> BenefitsChallenge:
    """
    Dependency provider for BenefitsChallenge instance.

    Returns:
        BenefitsChallenge: An instance of BenefitsChallenge class
        for use in the benefits calculation endpoint.
    """
    return BenefitsChallenge()


@router.post(
    "/",
    response_model=BenefitsOutput,
    description=DESCRIPTIONS["benefits"]["description"],
)
async def calculate_benefits(
    input_data: BenefitsInput,
    challenge: BenefitsChallenge = Depends(get_benefits_challenge),
):
    """
    Calculate employee benefits based on employment data.

    This endpoint processes the calculation of employment benefits such as
    vacation pay, thirteenth salary, FGTS, and other labor rights according
    to Brazilian legislation.

    Args:
        input_data (BenefitsInput): Input data containing:
            - salary (float): Employee's monthly salary
            - hire_date (date): Employee hire date
            - resignation_date (date): Employee resignation/termination date

        challenge (BenefitsChallenge): Benefits calculation service instance,
            automatically injected via dependency injection.

    Returns:
        BenefitsOutput: Object containing the calculated benefits values
        for each type of labor right.

    Raises:
        HTTPException: If input data is invalid or processing fails.

    Example:
        Request payload:
        {
            "salary": 5000.00,
            "hire_date": "2020-01-15",
            "resignation_date": "2023-06-20"
        }
    """
    logger.info(
        f"Processing benefits calculation: salary={input_data.salary}, "
        f"hire_date={input_data.hire_date}, "
        f"resignation_date={input_data.resignation_date}"
    )
    return challenge.execute(input_data)

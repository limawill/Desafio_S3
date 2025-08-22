from fastapi import APIRouter, Depends
from core.logging import logger
from core.description import DESCRIPTIONS
from core.validators import StringInput, StringOutput
from src.challenges.string_challenge import StringChallenge

router = APIRouter(prefix="/string")


def get_string_challenge() -> StringChallenge:
    """
    Dependency provider for StringChallenge instance.

    Returns:
        StringChallenge: An instance of StringChallenge class
        for use in the string processing endpoint.
    """
    return StringChallenge()


@router.post(
    "/", response_model=StringOutput, description=DESCRIPTIONS["string"]["description"]
)
async def check_string(
    input_data: StringInput, challenge: StringChallenge = Depends(get_string_challenge)
):
    """
    Process and analyze a string according to specific challenge rules.

    This endpoint performs various string operations and validations,
    which may include palindrome checking, anagram detection, pattern
    matching, or other string manipulation tasks.

    Args:
        input_data (StringInput): Input data containing:
            - string (str): The input string to be processed
            - Additional parameters for string processing rules
            as defined in StringInput

        challenge (StringChallenge): String processing service instance,
            automatically injected via dependency injection.

    Returns:
        StringOutput: Object containing the processing results,
        which may include validation outcomes, transformed strings,
        or analysis data.

    Raises:
        HTTPException: If input data is invalid or processing fails.

    Example:
        Request payload:
        {
            "string": "example input",
            // other processing parameters if applicable
        }
    """
    logger.info("Received request to check string")
    logger.info(f"Chegou na rota de verificação {input_data.text}")
    logger.info(f"Chegou na rota de verificação {input_data}")
    result = challenge.execute(input_data)
    return result

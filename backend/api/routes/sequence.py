from fastapi import APIRouter, Depends
from core.logging import logger
from core.description import DESCRIPTIONS
from core.validators import SequenceInput, SequenceOutput
from src.challenges.sequence_challenge import SequenceChallenge


router = APIRouter(prefix="/sequence")


def get_sequence_challenge() -> SequenceChallenge:
    """
    Dependency provider for SequenceChallenge instance.

    Returns:
        SequenceChallenge: An instance of SequenceChallenge class
        for use in the sequence calculation endpoint.
    """
    return SequenceChallenge()


@router.post(
    "/",
    response_model=SequenceOutput,
    description=DESCRIPTIONS["sequence"]["description"],
)
async def calculate_sequence(
    input_data: SequenceInput,
    challenge: SequenceChallenge = Depends(get_sequence_challenge),
):
    """
    Calculate a specific element in a mathematical sequence.

    This endpoint processes sequence challenges, typically involving
    mathematical sequences like Fibonacci, arithmetic, geometric,
    or other custom sequences.

    Args:
        input_data (SequenceInput): Input data containing:
            - position (int): The position in the sequence to calculate
            - Additional sequence parameters as defined in SequenceInput

        challenge (SequenceChallenge): Sequence calculation service instance,
            automatically injected via dependency injection.

    Returns:
        SequenceOutput: Object containing the calculated sequence value
        at the specified position and potentially additional
        sequence information.

    Raises:
        HTTPException: If input data is invalid or the calculation fails.

    Example:
        Request payload:
        {
            "position": 10,
            // other sequence parameters if applicable
        }
    """
    logger.info(f"Processing sequence challenge, position = {input_data.position}")
    return challenge.execute(input_data)

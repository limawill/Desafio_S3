from fastapi import APIRouter, Depends
from core.logging import logger
from core.description import DESCRIPTIONS
from src.challenges.board_game_challenge import BoardGameChallenge
from core.validators import BoardGameInput, BoardGameOutput


router = APIRouter(prefix="/board_game")


def get_board_game_challenge() -> BoardGameChallenge:
    """
    Dependency provider for BoardGameChallenge instance.

    Returns:
        BoardGameChallenge: An instance of BoardGameChallenge class
        for use in the board game solver endpoint.
    """
    return BoardGameChallenge()


@router.post(
    "/",
    response_model=BoardGameOutput,
    description=DESCRIPTIONS["board_game"]["description"],
)
async def solve_board_game(
    input_data: BoardGameInput,
    challenge: BoardGameChallenge = Depends(get_board_game_challenge),
):
    """
    Solve a board game challenge based on input parameters.

    This endpoint processes board game challenges, typically involving
    pathfinding, puzzle solving, or optimization problems on a game board.

    Args:
        input_data (BoardGameInput): Input data containing:
            - board_size (int): The dimensions of the game board
            - Additional board configuration parameters as
            defined in BoardGameInput

        challenge (BoardGameChallenge): Board game solver service instance,
            automatically injected via dependency injection.

    Returns:
        BoardGameOutput: Object containing the solution to the board game
        challenge, which may include paths, moves, or optimal configurations.

    Raises:
        HTTPException: If input data is invalid or no solution can be found.

    Example:
        Request payload:
        {
            "board_size": 8,
            // other board configuration parameters
        }
    """
    logger.info(
        f"Processing board game challenge, board_size = {input_data.board_size}"
    )
    return challenge.execute(input_data)

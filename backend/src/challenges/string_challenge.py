from core.logging import logger
from src.challenges.base_challenge import IChallenge
from core.validators import StringInput, StringOutput


class StringChallenge(IChallenge):
    """
    Challenge implementation for string validation based on specific criteria.

    This class validates whether a given string meets the required pattern:
    the string must start with the character 'B' and end with the character 'A'.

    The validation is case-sensitive and considers exact character matching.

    Inherits from:
        IChallenge: Base interface for challenge implementations
    """

    def execute(self, input_data: StringInput) -> StringOutput:
        """
        Validate if the input string meets the required pattern criteria.

        The validation checks if the string:
        1. Starts with the uppercase character 'B'
        2. Ends with the uppercase character 'A'

        Args:
            input_data (StringInput): Input data containing:
                - text (str): The string to be validated

        Returns:
            StringOutput: Object containing the validation result:
                - is_valid (bool): True if the string meets the criteria,
                                False otherwise

        Example:
            "BA" → True (starts with 'B', ends with 'A')
            "BCA" → True (starts with 'B', ends with 'A')
            "ABC" → False (starts with 'A', not 'B')
            "BCD" → False (ends with 'D', not 'A')
            "ba" → False (case-sensitive - lowercase 'b' and 'a')
            "B" → False (must start AND end with specified characters)
            "A" → False (must start AND end with specified characters)
            "" → False (empty string doesn't meet criteria)

        Note:
            Validation is case-sensitive. Only uppercase 'B' and 'A'
            are accepted.

            The string must have at least 2 characters to satisfy
            both conditions.
        """
        logger.info(f"Processing string: {input_data}")
        logger.info(f"Processing string: {input_data.text}")
        text = input_data.text
        is_valid = text.startswith("B") and text.endswith("A")
        logger.info(f"StringChallenge result: {is_valid}")
        return StringOutput(is_valid=is_valid)

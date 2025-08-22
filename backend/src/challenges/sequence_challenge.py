from src.challenges.base_challenge import IChallenge
from core.validators import SequenceInput, SequenceOutput


class SequenceChallenge(IChallenge):
    """
    Challenge implementation for calculating values in a mathematical sequence.

    This class handles the calculation of sequence values based on a specific
    mathematical pattern. The sequence follows an arithmetic progression
    starting from 11 with a common difference of 7.

    Sequence formula: aₙ = 11 + (n - 1) * 7
    Where:
        aₙ = value at position n
        n = position in the sequence (1-indexed)

    Inherits from:
        IChallenge: Base interface for challenge implementations
    """

    def execute(self, input_data: SequenceInput) -> SequenceOutput:
        """
        Calculate the sequence value at the specified position.

        The sequence is defined as an arithmetic progression starting at 11
        with a common difference of 7 between consecutive terms.

        Args:
            input_data (SequenceInput): Input data containing:
                - position (int): The 1-indexed position in the
                sequence to calculate (position >= 1)

        Returns:
            SequenceOutput: Object containing the calculated sequence value:
                - value (int): The value at the specified position in
                the sequence

        Raises:
            ValueError: If position is less than 1

        Example:
            position = 1 → value = 11
            position = 2 → value = 18
            position = 3 → value = 25
            position = 4 → value = 32

        Note:
            The sequence uses 1-indexed positions (first element is
            at position 1)
        """
        position = input_data.position
        result = 11 + (position - 1) * 7
        return SequenceOutput(result=result)

from typing import List
from collections import deque
from core.logging import logger
from src.challenges.base_challenge import IChallenge
from core.validators import BoardGameInput, BoardGameOutput


class BoardGameChallenge(IChallenge):
    """
    Challenge implementation for solving board game pathfinding problems.

    This class handles calculations for a board game where players can make
    fixed jumps (based on board values) or free jumps to any subsequent
    position.
    It provides three metrics: minimum turns, success probability, and path
    combinations.

    Inherits from:
        IChallenge: Base interface for challenge implementations
    """

    def execute(self, input_data: BoardGameInput) -> BoardGameOutput:
        """
        Solve the board game challenge and calculate all required metrics.

        Args:
            input_data (BoardGameInput): Input data containing:
                - board_size (int): The size of the game board (n x n)
                - board (List[int]): List of integers representing board
                cell values

        Returns:
            BoardGameOutput: Object containing calculated results:
                - turns (int): Minimum number of turns to reach the end
                - probability (float): Probability of successfully reaching
                the end
                - combinations (int): Number of possible paths to reach
                the end

        Raises:
            ValueError: If board validation fails or inputs are invalid
        """
        n = input_data.board_size
        board = input_data.board

        # Validação básica
        if len(board) != n:
            return BoardGameOutput(turns=0, probability=0.0, combinations=0)

        # Menor número de turnos (BFS)
        min_turns = self._min_turns(n, board)

        # Probabilidade de sucesso (DP)
        probability = self._probability(n, board)

        # Número de combinações (DP)
        combinations = self._combinations(n, board)

        logger.info(f"BoardGameChallenge results: turns={min_turns}")
        logger.info(f"BoardGameChallenge results: probability={probability}")
        logger.info(f"BoardGameChallenge results: combinations={combinations}")
        return BoardGameOutput(
            turns=min_turns, probability=probability, combinations=combinations
        )

    def _min_turns(self, n: int, board: List[int]) -> int:
        """
        Calculate the minimum number of turns to reach the end using BFS.

        Players can make:
        - Fixed jump: move forward by board[i] positions from position i
        - Free jumps: move to any position j where j > i

        Args:
            n (int): Size of the board
            board (List[int]): List of integers representing board cell values

        Returns:
            int: Minimum number of turns required to reach position n-1
                Returns 0 if unreachable or invalid input
        """
        if n <= 1:
            return 0

        min_turns = [float("inf")] * n
        min_turns[0] = 0
        queue = deque([(0, 0)])  # (posição, turnos)
        visited = set([0])

        while queue:
            pos, turns = queue.popleft()
            if pos == n - 1:
                return turns

            # Pulo fixo
            next_pos = pos + board[pos]
            if next_pos < n and next_pos not in visited:
                min_turns[next_pos] = min(min_turns[next_pos], turns + 1)
                queue.append((next_pos, turns + 1))
                visited.add(next_pos)

            # Pulos livres
            for j in range(pos + 1, n):
                if j not in visited:
                    min_turns[j] = min(min_turns[j], turns + 1)
                    queue.append((j, turns + 1))
                    visited.add(j)

        return min_turns[n - 1] if min_turns[n - 1] != float("inf") else 0

    def _probability(self, n: int, board: List[int]) -> float:
        """
        Calculate the probability of successfully reaching the end using
        dynamic programming.

        Assumes uniform probability distribution for all possible moves from
        each position.

        Args:
            n (int): Size of the board
            board (List[int]): List of integers representing board cell values

        Returns:
            float: Probability of reaching the end from the start
            position (0 to 1.0)
            Returns 0.0 if unreachable or invalid input
        """
        if n <= 1:
            return 0.0

        dp = [0.0] * n
        dp[n - 1] = 1.0  # Chegou ao destino

        for i in range(n - 2, -1, -1):
            possible_jumps = []
            # Pulo fixo
            next_pos = i + board[i]
            if next_pos < n:
                possible_jumps.append(next_pos)
            # Pulos livres
            for j in range(i + 1, n):
                possible_jumps.append(j)

            if possible_jumps:
                dp[i] = sum(dp[j] for j in possible_jumps) / len(possible_jumps)

        return dp[0]

    def _combinations(self, n: int, board: List[int]) -> int:
        """
        Calculate the number of distinct paths to reach the end using
        dynamic programming.

        Args:
            n (int): Size of the board
            board (List[int]): List of integers representing board cell values

        Returns:
            int: Number of distinct paths from start to end position
                Returns 0 if unreachable or invalid input
        """
        if n <= 1:
            return 0

        dp = [0] * n
        dp[n - 1] = 1  # Um caminho para o destino

        for i in range(n - 2, -1, -1):
            possible_jumps = []
            # Pulo fixo
            next_pos = i + board[i]
            if next_pos < n:
                possible_jumps.append(next_pos)
            # Pulos livres
            for j in range(i + 1, n):
                possible_jumps.append(j)

            dp[i] = sum(dp[j] for j in possible_jumps)

        return dp[0]

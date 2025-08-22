from pydantic import BaseModel
from abc import ABC, abstractmethod


class IChallenge(ABC):
    @abstractmethod
    def execute(self, input_data: BaseModel) -> BaseModel:
        """Executa a lógica do desafio.

        Args:
            input_data (BaseModel): Dados de entrada validados pelo Pydantic.

        Returns:
            BaseModel: Dados de saída validados pelo Pydantic.
        """
        pass

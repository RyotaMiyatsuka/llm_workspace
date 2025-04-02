from abc import ABC, abstractmethod

from pydantic import BaseModel

from domain.domain_models.value_objects.prompt import Messages


class ILlmCaller(ABC):
    """LLM呼び出し."""

    def __init__(self) -> None:
        """コンストラクタ."""
        super().__init__()

    @abstractmethod
    def generate(
        self,
        messages: Messages,
        response_format: dict | BaseModel | None = None,
        response_choices: list | None = None,
    ) -> str:
        """回答生成."""
        raise NotImplementedError

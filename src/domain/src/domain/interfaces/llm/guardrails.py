from abc import ABC, abstractmethod

from domain.domain_models.value_objects.llm_check_results import LLMCheckResult
from domain.domain_models.value_objects.prompt import Messages


class IGuardRails(ABC):
    """LLMの入出力チェック."""

    def __init__(self) -> None:
        """コンストラクタ."""
        super().__init__()

    @abstractmethod
    def check_input(
        self,
        messages: Messages,
    ) -> LLMCheckResult:
        """LLMの入力チェック."""
        raise NotImplementedError

    @abstractmethod
    def check_output(self, messages: Messages, response: str) -> LLMCheckResult:
        """LLMの出力チェック."""

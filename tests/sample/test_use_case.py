from unittest.mock import Mock

from domain.domain_models.entities.chat_history import ChatHistory
from domain.domain_models.value_objects.llm_check_results import LLMCheckResult
from domain.interfaces.llm.guardrails import IGuardRails
from domain.interfaces.llm.llm_caller import ILlmCaller
from domain.interfaces.repositories.chat_history import IChatHistoryRepository
from use_case.chat import ChatAppService


class TestChatInvokeUseCaseErrorHandling:
    """ユースケースエラーハンドリングテスト."""

    def setup_method(self) -> None:
        """各テストメソッドの前に実行."""
        self.chat_hist_repository = Mock(spec=IChatHistoryRepository)
        self.llm_caller = Mock(spec=ILlmCaller)
        self.guard_rails = Mock(spec=IGuardRails)
        self.use_case = ChatAppService(
            llm_caller=self.llm_caller,
            guard_rails=self.guard_rails,
            chat_history_repository=self.chat_hist_repository,
        )

    def test_input_check_error(
        self,
        failed_llm_check_result: LLMCheckResult,
        default_chat_history: ChatHistory,
    ) -> None:
        """入力チェックでエラーだった場合のテスト."""
        self.guard_rails.check_input.return_value = failed_llm_check_result

        result = self.use_case.invoke(
            user_input="サンプルプロンプト",
            chat_history=default_chat_history.model_dump(),
        )

        assert result == "インプットチェックエラー"

# tests/domain/test_use_cases.py
from unittest.mock import Mock

from domain.interfaces.llm.guardrails import IGuardRails
from domain.interfaces.llm.llm_caller import ILlmCaller
from domain.interfaces.repositories.chat_history import IChatHistoryRepository
from use_case.chat import ChatAppService


class TestChatInvokeUseCaseErrorHandling:
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

    def test_input_check_runtime_error(
        self, default_llm_check_result, default_chat_history
    ) -> None:
        """入力チェックでRuntimeErrorが発生したときのテスト."""
        self.guard_rails.check_input.side_effect = RuntimeError()

        result = self.use_case.invoke(
            user_input="サンプルプロンプト", chat_history=default_chat_history
        )

        assert result == "インプットチェックエラー"

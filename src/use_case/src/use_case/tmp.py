from typing import override

from domain.interfaces.llm.guardrails import IGuardRails
from domain.interfaces.llm.llm_caller import ILlmCaller
from domain.interfaces.repositories.chat_history import IChatHistoryRepository
from use_case.chat import ChatAppService


class MockLLMCaller(ILlmCaller):
    """モック."""

    @override
    def generate(self, messages, response_format=None, response_choices=None):
        return "モック LLM Caller generate"


class MockGuardRails(IGuardRails):
    """モック."""

    @override
    def check_input(self, messages):
        return "モックinチェック"

    @override
    def check_output(self, messages, response):
        return "モックoutチェック"


class MockChatHistoryRepository(IChatHistoryRepository):
    """モック."""

    @override
    def save(self, chat_history):
        print("save 完了")

    @override
    def find_by_id(self, chat_id):
        return "find by id"

    @override
    def delete(self, chat_id):
        return "delete"


chatapp = ChatAppService(
    llm_caller=MockLLMCaller(),
    guard_rails=MockGuardRails(),
    chat_history_repository=MockChatHistoryRepository(),
)

answer = chatapp.invoke(user_input="架空のシステム障害を考えてください。")
print(answer)

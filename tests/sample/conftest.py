from fastapi.testclient import TestClient
from pytest import fixture

from domain.common.value_define.enums import LLMCheckType, Role
from domain.domain_models.entities.chat_history import ChatHistory
from domain.domain_models.value_objects.llm_check_results import LLMCheckResult
from domain.domain_models.value_objects.prompt import Messages, PromptElement
from presentation.main import app


@fixture
def client() -> TestClient:
    """FastApiサーバーのテストクライアントを返す."""
    return TestClient(app)


@fixture
def default_llm_check_result() -> LLMCheckResult:
    """デフォルトチェック結果."""
    return LLMCheckResult(success=True, check_type=LLMCheckType.POLICY_CHECK)


@fixture
def failed_llm_check_result() -> LLMCheckResult:
    """チェック失敗."""
    return LLMCheckResult(success=False, check_type=LLMCheckType.POLICY_CHECK)


@fixture
def default_chat_history() -> ChatHistory:
    message = PromptElement(role=Role.USER, content="デフォルトコンテント")
    return ChatHistory(
        chat_id="00000000-0000-0000-0000-000000000000",
        messages=Messages(messages=[message]),
    )

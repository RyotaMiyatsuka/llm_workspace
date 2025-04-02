from enum import Enum, StrEnum


class Role(StrEnum):
    """ロール."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    CONTEXT = "context"


class LLMCheckType(Enum):
    """LLM入出力チェック種別."""

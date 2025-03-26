from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, StringConstraints


class Role(StrEnum):
    """ロール."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    CONTEXT = "context"


class Prompt(BaseModel):
    """プロンプト1要素."""

    role: Role
    content: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class Message(BaseModel):
    """実行プロンプト."""

    message: list[Prompt]

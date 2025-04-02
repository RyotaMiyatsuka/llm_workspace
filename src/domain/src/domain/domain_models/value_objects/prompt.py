from typing import Annotated, Self

from pydantic import BaseModel, Field, StringConstraints

from domain.common.value_define.enums import Role


class PromptElement(BaseModel, frozen=True):
    """プロンプト1要素."""

    role: Role
    content: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class Messages(BaseModel, frozen=True):
    """実行プロンプト."""

    messages: list[PromptElement] = Field(min_length=1)

    def add_prompt_element(self, role: Role, content: str) -> Self:
        """プロンプトを追加して返す."""
        new_messages = [*self.messages, PromptElement(role=role, content=content)]
        return Messages(messages=new_messages)

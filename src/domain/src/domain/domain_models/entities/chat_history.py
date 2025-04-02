from uuid import UUID

from pydantic import BaseModel

from domain.domain_models.value_objects.prompt import Messages


class ChatHistory(BaseModel):
    """チャット履歴."""

    chat_id: UUID
    messages: Messages

from pydantic import BaseModel


# TODO: 定義
class ChatRequest(BaseModel):
    """チャットAPIのリクエスト."""


# TODO: 定義
class ChatResponse(BaseModel):
    """チャットAPIのレスポンス."""

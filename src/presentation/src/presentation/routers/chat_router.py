# presentation/api/routers/user_router.py
from fastapi import APIRouter

# ルーターの作成
router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_chats():
    """チャット一覧."""


@router.get("/{chat_id}")
def get_chat_room():
    """チャットルーム."""


@router.post("/{chat_id}")
def create_chat():
    """新チャットルーム作成."""


@router.post("/{chat_id}/invoke")
def invoke():
    """チャット回答生成."""

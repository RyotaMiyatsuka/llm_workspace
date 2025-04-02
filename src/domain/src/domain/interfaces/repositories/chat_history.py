from abc import ABC, abstractmethod

from domain.domain_models.entities.chat_history import ChatHistory


class IChatHistoryRepository(ABC):
    """チャット履歴リポジトリ."""

    def __init__(self) -> None:
        """コンストラクタ."""
        super().__init__()

    @abstractmethod
    def save(self, chat_history: ChatHistory) -> None:
        """オブジェクトを保存する."""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, chat_id: str) -> ChatHistory:
        """チャット履歴を取得する."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, chat_id: str) -> None:
        """チャット履歴を削除する."""
        raise NotImplementedError

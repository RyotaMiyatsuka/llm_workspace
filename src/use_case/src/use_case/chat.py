from uuid import uuid4

from domain.common.value_define.enums import Role
from domain.domain_models.entities.chat_history import ChatHistory
from domain.domain_models.value_objects.prompt import Messages, PromptElement
from domain.interfaces.llm.guardrails import IGuardRails
from domain.interfaces.llm.llm_caller import ILlmCaller
from domain.interfaces.repositories.chat_history import IChatHistoryRepository


class ChatAppService:
    """チャットのユースケース."""

    llm_caller: ILlmCaller
    guard_rails: IGuardRails
    chat_history_repository: IChatHistoryRepository

    def __init__(
        self,
        llm_caller: ILlmCaller,
        guard_rails: IGuardRails,
        chat_history_repository: IChatHistoryRepository,
    ) -> None:
        """コンストラクタ."""
        self.llm_caller = llm_caller
        self.guard_rails = guard_rails
        self.chat_history_repository = chat_history_repository

    def invoke(self, user_input: str, chat_history: dict | None = None) -> str:
        """ユーザーの入力に対して回答を生成する."""
        # メッセージリストを作成
        current_elem = PromptElement(role=Role.USER, content=user_input)
        if chat_history is None:
            # 新規メッセージ作成
            current_messages = Messages(messages=[current_elem])
        else:
            # 過去チャットをモデルにマッピング
            chat_history_obj = ChatHistory(**chat_history)
            past_messages = chat_history_obj.messages
            # メッセージを更新
            current_messages = past_messages.add_prompt_element(elem=current_elem)

        # LLM入力チェック
        input_check_result = self.guard_rails.check_input(messages=current_messages)
        # TODO: チェックエラー時処理
        if input_check_result.success is False:
            return None

        # 回答生成処理の呼び出し
        answer = self.llm_caller.generate(messages=current_messages)

        # LLM出力チェック
        output_check_result = self.guard_rails.check_output(
            messages=current_messages, response=answer
        )
        # TODO: チェックエラー時処理
        if output_check_result.success is False:
            return None

        # 会話の更新
        new_messages = current_messages.add_prompt_element(
            role=Role.ASSISTANT, content=answer
        )
        new_chat_history = ChatHistory(chat_id=uuid4(), messages=new_messages)

        # TODO: 会話の保存
        self.chat_history_repository.save(new_chat_history)

        return answer

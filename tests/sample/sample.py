# tests/domain/test_use_cases.py
from unittest.mock import Mock

from domain.entities import User
from domain.interfaces.llm.guardrails import IGuardRails
from domain.interfaces.llm.llm_caller import ILlmCaller
from domain.interfaces.repositories.chat_history import IChatHistoryRepository
from use_case.chat import ChatAppService


class TestChatInvokeUseCaseErrorHandling:
    def setup_method(self) -> None:
        """各テストメソッドの前に実行."""
        self.chat_hist_repository = Mock(spec=IChatHistoryRepository)
        self.llm_caller = Mock(spec=ILlmCaller)
        self.guard_rails = Mock(spec=IGuardRails)
        self.use_case = ChatAppService(self.repository)

    def test_input_check_runtime_error(self) -> None:
        """入力チェックでRuntimeErrorが発生したときのテスト."""
        self.guard_rails.check_input.side_effect = RuntimeError()

    # サンプル
    def test_get_user_repository_runtime_error(self) -> None:
        """リポジトリでRuntimeErrorが発生した場合のエラーハンドリングをテスト."""
        # リポジトリのget_by_idメソッドがRuntimeErrorを発生させるように設定
        error_message = "データベース接続エラー"
        self.repository.get_by_id.side_effect = RuntimeError(error_message)

        # ユースケースを実行
        result = self.use_case.execute(user_id=1)

        # 検証
        assert result.success is False
        assert "Database error" in result.error
        assert error_message in result.error
        assert result.error_code == "DATABASE_ERROR"
        assert result.user is None
        # リポジトリのメソッドが呼ばれたことを確認
        self.repository.get_by_id.assert_called_once_with(1)

    def test_get_user_repository_unexpected_error(self):
        """予期しない例外が発生した場合のエラーハンドリングをテスト"""
        # 予期しない例外を発生させる
        error_message = "未知のエラー"
        self.repository.get_by_id.side_effect = KeyError(error_message)

        # ユースケースを実行
        result = self.use_case.execute(user_id=1)

        # 検証
        assert result.success is False
        assert "Unexpected error" in result.error
        assert result.error_code == "UNEXPECTED_ERROR"
        assert result.user is None
        # リポジトリのメソッドが呼ばれたことを確認
        self.repository.get_by_id.assert_called_once_with(1)

    def test_get_user_not_found(self):
        """ユーザーが見つからない場合のエラーハンドリングをテスト"""
        # リポジトリがNoneを返すように設定
        self.repository.get_by_id.return_value = None

        # ユースケースを実行
        result = self.use_case.execute(user_id=999)

        # 検証
        assert result.success is False
        assert "User with id 999 not found" in result.error
        assert result.error_code == "USER_NOT_FOUND"
        assert result.user is None
        # リポジトリのメソッドが呼ばれたことを確認
        self.repository.get_by_id.assert_called_once_with(999)

    def test_get_user_success(self):
        """正常系のテスト（比較のため）"""
        # モックの設定
        mock_user = User(id=1, name="山田太郎", email="yamada@example.com", age=30)
        self.repository.get_by_id.return_value = mock_user

        # ユースケースを実行
        result = self.use_case.execute(user_id=1)

        # 検証
        assert result.success is True
        assert result.user == mock_user
        assert result.error is None
        assert result.error_code is None
        # リポジトリのメソッドが呼ばれたことを確認
        self.repository.get_by_id.assert_called_once_with(1)

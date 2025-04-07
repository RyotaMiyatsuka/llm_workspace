from fastapi.testclient import TestClient


class TestChatPresentation:
    """チャットプレゼンテーション層のテスト."""

    def setup_method(self) -> None:
        """各テストメソッドの前に実行."""

    def test_connection_check(self, client: TestClient) -> None:
        """コネクションチェックのテスト."""
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"message": "Hello World!"}

from fastapi import FastAPI

# from presentation.error_handlers import register_exception_handlers
from presentation.routers import chat_router

app = FastAPI(title="クリーンアーキテクチャAPI")

# TODO: エラーハンドラを登録
# register_exception_handlers(app)

# ルーターをアプリケーションに含める
app.include_router(chat_router.router)


@app.get("/")
async def root() -> dict[str, str]:
    """ルートパス."""
    return {"message": "Hello World!"}

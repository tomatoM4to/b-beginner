from fastapi import FastAPI
import uvicorn
from app.common.config import conf

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI()
    c = conf()

    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    return app

app = create_app()


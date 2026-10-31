"""应用配置：从环境变量 / .env 读取"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # 应用
    APP_NAME: str = "Meet · 研发会议垂类 Agent"
    DEBUG: bool = True
    SERVER_PORT: int = 8787

    # 数据库
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/meeting"
    DATABASE_ECHO: bool = False

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # 文件上传
    UPLOAD_DIR: str = "./uploads"

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

settings = Settings()
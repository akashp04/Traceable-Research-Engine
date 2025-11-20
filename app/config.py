from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "TREngine"
    app_description: str = "A powerful Deep Research Engine"
    app_version: str = "1.0.0"
    host: str = "localhost"
    port: int = 8000
    reload: bool = True
    log_level: str = "info"

    environment: str = "development"
    
    OPENAI_API_KEY: str = Field(default="")
    
    MAX_STEPS: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
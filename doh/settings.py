from pydantic import BaseSettings


class Settings(BaseSettings):
    enable_openai: bool = False
    openai_api_key: str | None = None


settings = Settings()

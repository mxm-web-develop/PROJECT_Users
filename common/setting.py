from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: Optional[str] = None
    secret_key: Optional[str] = None
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

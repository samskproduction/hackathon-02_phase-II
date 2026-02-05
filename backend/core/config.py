from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    FRONTEND_URL: Optional[str] = "http://localhost:3000"
    BACKEND_URL: Optional[str] = "http://localhost:8000"
    BETTER_AUTH_SECRET: str
    NEON_DB_URL: str
    DEBUG: Optional[bool] = True

    model_config = {"env_file": ".env"}

settings = Settings()

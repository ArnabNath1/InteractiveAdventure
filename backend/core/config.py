from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator
import os

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_URL: Optional[str] = None
    DATABASE_PATH: Optional[str] = "databse.db"  # Add this field

    ALLOWED_ORIGINS: str = ""

    GEMINI_API_KEY: str

    def __init__(self, **values):
        super().__init__(**values)
        
        # Use SQLite by default if DATABASE_URL is not provided or in DEBUG mode
        if not self.DATABASE_URL:
            # Use DATABASE_PATH from env or default
            db_path = self.DATABASE_PATH or "databse.db"
            self.DATABASE_URL = f"sqlite:///./{db_path}"
        elif not self.DEBUG and os.getenv("DB_USER"):
            # Only use PostgreSQL if explicitly configured
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_name = os.getenv("DB_NAME")
            self.DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
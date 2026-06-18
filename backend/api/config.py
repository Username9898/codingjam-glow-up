"""Configuration settings for the application"""

from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path


class Settings(BaseSettings):
    """Application settings from environment variables"""

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
    ]

    # Image Processing
    MAX_IMAGE_SIZE_MB: int = 50
    ALLOWED_FORMATS: str = "jpg,jpeg,png,webp"
    TARGET_IMAGE_SIZE: int = 640
    JPEG_QUALITY: int = 85

    # Storage
    UPLOAD_DIR: str = "./uploads"
    OUTPUT_DIR: str = "./outputs"
    CLEANUP_HOURS: int = 24

    # Processing
    PROCESSING_TIMEOUT: int = 30
    MAX_WORKERS: int = 4

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

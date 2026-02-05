from sqlmodel import create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv
from core.config import settings
import logging

logger = logging.getLogger(__name__)

load_dotenv()

try:
    # Create database engine with Neon-specific configuration
    engine = create_engine(
        settings.NEON_DB_URL,
        connect_args={
            "sslmode": "require"
            # Note: Removed channel_binding as it's not supported by Neon
        },
        pool_recycle=300,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )
    logger.info("Database engine created successfully")
except Exception as e:
    logger.error(f"Failed to create database engine: {e}")
    raise

def get_session() -> Generator[Session, None, None]:
    """Get database session with error handling"""
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        logger.error(f"Database session error: {e}")
        raise

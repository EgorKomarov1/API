from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from src.config import database_url
from src.logger import logger


engine = create_engine(
    database_url,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)


@contextmanager
def get_db_context() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(e)
        raise
    finally:
        session.close()


def test_connection() -> bool:
    try:
        with get_db_context() as session:
            result = session.execute(text("SELECT 1"))
            return result.fetchone() is not None
    except Exception as e:
        logger.error(e)
        return False

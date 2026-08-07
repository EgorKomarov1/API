from sqlalchemy import create_engine, text
from src.config import database_url
from src.logger import logger
from contextlib import contextmanager


engine = create_engine(
    database_url,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)


@contextmanager
def get_db_context():
    conn = engine.connect()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        logger.error(e)
        raise
    finally:
        conn.close()


def test_connection() -> bool:
    try:
        with get_db_context() as conn:
            result = conn.execute(text("SELECT 1"))
            return result.fetchone() is not None
    except Exception as e:
        logger.error(e)
        return False

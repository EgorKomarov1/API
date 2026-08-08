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
    with engine.begin() as conn:
        try:
            yield conn
        except Exception as e:
            logger.error(e)
            raise

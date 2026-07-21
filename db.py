from contextlib import contextmanager
from typing import Generator
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

from config import database_url
from logger import logger

_connection_pool: pool.ThreadedConnectionPool | None = None


def init_connection_pool() -> pool.ThreadedConnectionPool:
    global _connection_pool

    if _connection_pool is not None:
        return _connection_pool

    try:
        _connection_pool = pool.ThreadedConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=database_url
        )
        return _connection_pool
    except Exception as e:
        logger.error(e)
        raise


def _get_pool() -> pool.ThreadedConnectionPool:
    if _connection_pool is None:
        return init_connection_pool()
    return _connection_pool


@contextmanager
def get_db_context() -> Generator[RealDictCursor, None, None]:
    db_pool = _get_pool()
    conn = None
    cursor = None
    try:
        conn = db_pool.getconn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        yield cursor
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(e)
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            db_pool.putconn(conn)


def test_connection() -> bool:
    try:
        with get_db_context() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(e)
        return False

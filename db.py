from typing import cast

from psycopg2.extras import RealDictCursor
from psycopg2 import pool

from config import database_url
from logger import logger

from contextlib import contextmanager


connection_pool: pool.SimpleConnectionPool | None = None
_pool_initialized = False


def init_connection_pool():
    global connection_pool, _pool_initialized

    if _pool_initialized:
        return connection_pool

    try:
        connection_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=database_url
        )
        _pool_initialized = True
        return connection_pool
    except Exception as e:
        logger.error(e)
        raise


def get_db_connection():
    global connection_pool

    if connection_pool is None:
        init_connection_pool()

    pool_instance = cast(pool.SimpleConnectionPool, connection_pool)

    try:
        return pool_instance.getconn()
    except Exception as e:
        logger.error(e)
        raise


def return_db_connection(conn):
    global connection_pool

    pool_instance = cast(pool.SimpleConnectionPool, connection_pool)

    try:
        pool_instance.putconn(conn)
    except Exception as e:
        logger.error(e)


@contextmanager
def get_db_context():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        yield cursor
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            return_db_connection(conn)


def test_connection() -> bool:
    try:
        with get_db_context() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(e)
        return False

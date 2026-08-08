from sqlalchemy import create_engine, text
from src.config import database_url


engine = create_engine(
    database_url,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)

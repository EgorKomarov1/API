from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db import test_connection, engine
from src.logger import logger
from src.api import v1_router, v2_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Запуск")

    if test_connection():
        logger.info("Работает")
    else:
        logger.warning("Не работает")

    yield

    engine.dispose()

    logger.info("Не работает")


app = FastAPI(
    title="API",
    version="2.0.0",
    debug=True,
    lifespan=lifespan
)

app.include_router(v1_router)
app.include_router(v2_router)


@app.get("/v1")
def root():
    return {
        "message": "API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/v2")
def root():
    return {
        "message": "API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health_check():
    db_ok = test_connection()
    return {
        "status": "healthy" if db_ok else "unhealthy",
        "database": "connected" if db_ok else "disconnected"
    }

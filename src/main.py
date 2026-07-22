from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import test_connection, init_connection_pool
from src.logger import logger
from src.api.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Запуск")

    init_connection_pool()

    if test_connection():
        logger.info("Работает")
    else:
        logger.warning("Не работает")

    yield

    logger.info("Не работает")


app = FastAPI(
    title="API",
    version="1.0.0",
    debug=True,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "API",
        "version": "1.0.0",
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


app.include_router(router)

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db import engine
from src.logger import logger
from src.api.v2.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Запуск")

    yield

    engine.dispose()

    logger.info("Не работает")


app = FastAPI(
    title="API",
    version="2.0.0",
    debug=True,
    lifespan=lifespan
)

app.include_router(router)

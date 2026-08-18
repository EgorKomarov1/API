from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database.db import engine
from src.logger import logger
from src.routing.v2.routers import router
from src.middlewares.process_time import add_process_time_header


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

app.middleware('http')(add_process_time_header)

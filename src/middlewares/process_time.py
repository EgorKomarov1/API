import time
from fastapi import Request
from src.logger import logger


async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    logger.info("%s %s выполнилось за %s", request.method, request.url.path, process_time)

    return response

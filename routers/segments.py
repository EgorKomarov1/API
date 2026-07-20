from fastapi import APIRouter, Query
from db import get_db_context

router = APIRouter(prefix="/segments", tags=["segments"])


@router.get("/")
def get_segments(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT flight_id
                                ,fare_conditions
                                ,price
                          FROM bookings.segments
                          GROUP BY flight_id, fare_conditions, price
                          ORDER BY price
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()

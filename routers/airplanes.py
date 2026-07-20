from fastapi import APIRouter, Query
from db import get_db_context

router = APIRouter(prefix="/airplanes", tags=["airplanes"])


@router.get("/")
def get_airplanes(limit: int = Query(50, ge=1, le=1000),
                  page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT airplane_code
                               , model
                               , range
                               , speed
                          FROM bookings.airplanes_data
                          ORDER BY range DESC
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()

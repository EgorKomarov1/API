
from fastapi import APIRouter, Query
from db import get_db_context

router = APIRouter(prefix="/flights", tags=["flights"])


@router.get("/")
def get_flights(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1, le=1000)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT route_no
                               , scheduled_departure
                               , scheduled_arrival
                               , scheduled_arrival - scheduled_departure AS duration
                          FROM bookings.flights
                          WHERE status = 'Scheduled'
                          ORDER BY scheduled_departure
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()

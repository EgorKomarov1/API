from fastapi import APIRouter, Query
from db import get_db_context

router = APIRouter(prefix="/passengers", tags=["passengers"])


@router.get("/")
def get_passengers(limit: int = Query(50, ge=1, le=1000),
                   page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""
                          SELECT passenger_id
                               , passenger_name
                               , s.ticket_no
                               , flight_id
                               , fare_conditions
                               , book_ref
                               , price
                               , outbound
                          FROM bookings.segments s
                                   JOIN bookings.tickets t on t.ticket_no = s.ticket_no
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()

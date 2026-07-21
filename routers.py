from fastapi import APIRouter, Query
from db import get_db_context

router = APIRouter()


@router.get("/airplanes", tags=['airplanes'])
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


@router.get("/airports", tags=['airports'])
def get_airports(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT airport_code
                               , airport_name
                               , city, country
                               , coordinates
                               , timezone
                          FROM bookings.airports_data
                          ORDER BY airport_code
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/boarding_passes", tags=['boarding_passes'])
def get_boarding_passes(limit: int = Query(50, ge=1, le=1000),
                        page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT ticket_no
                               , flight_id
                               , seat_no
                               , boarding_no
                               , boarding_time
                          FROM bookings.boarding_passes
                          ORDER BY boarding_time
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/bookings", tags=['bookings'])
def get_bookings(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT book_ref
                               , book_date
                               , total_amount
                          FROM bookings.bookings
                          ORDER BY book_date
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/flights", tags=['flights'])
def get_flights(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
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


@router.get("/passengers", tags=['passengers'])
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
                          ORDER BY passenger_id
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/routes", tags=['routes'])
def get_routes(limit: int = Query(50, ge=1, le=1000),
               page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT route_no
                               , validity
                               , departure_airport
                               , arrival_airport
                               , airplane_code
                               , days_of_week
                               , scheduled_time
                               , duration
                          FROM bookings.routes
                          ORDER BY route_no
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/segments", tags=['segments'])
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


@router.get("/seats", tags=['seats'])
def get_seats(limit: int = Query(50, ge=1, le=1000),
              page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT airplane_code
                               , seat_no
                               , fare_conditions
                          FROM bookings.seats
                          ORDER BY airplane_code, seat_no
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()


@router.get("/tickets", tags=['tickets'])
def get_tickets(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    with get_db_context() as cursor:
        cursor.execute("""SELECT ticket_no
                               , book_ref
                               , passenger_id
                               , passenger_name
                               , outbound
                          FROM bookings.tickets
                          ORDER BY ticket_no
                          LIMIT %s OFFSET %s""", (limit, (page - 1) * limit)
                       )
        return cursor.fetchall()

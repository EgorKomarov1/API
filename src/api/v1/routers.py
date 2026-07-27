from fastapi import APIRouter, Query
from src.db import get_db_context
from sqlalchemy import text
from src.api.v1.schemas import Airplane, Airport, BoardingPass, Booking, Flight, Route, Seat, Segment, Ticket, Passenger

router = APIRouter()


@router.get("/airplanes", tags=['airplanes'], response_model=list[Airplane])
def get_airplanes(limit: int = Query(50, ge=1, le=1000),
                  page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT airplane_code
                         , model
                         , range
                         , speed
                    FROM bookings.airplanes_data
                    ORDER BY range DESC
                    LIMIT :limit OFFSET :offset""")

    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/airports", tags=['airports'], response_model=list[Airport])
def get_airports(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT airport_code
                         , airport_name
                         , city, country
                         , coordinates
                         , timezone
                    FROM bookings.airports_data
                    ORDER BY airport_code
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/boarding_passes", tags=['boarding_passes'], response_model=list[BoardingPass])
def get_boarding_passes(limit: int = Query(50, ge=1, le=1000),
                        page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT ticket_no
                         , flight_id
                         , seat_no
                         , boarding_no
                         , boarding_time
                    FROM bookings.boarding_passes
                    ORDER BY boarding_time
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/bookings", tags=['bookings'], response_model=list[Booking])
def get_bookings(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT book_ref
                         , book_date
                         , total_amount
                    FROM bookings.bookings
                    ORDER BY book_date
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/flights", tags=['flights'], response_model=list[Flight])
def get_flights(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT route_no
                         , scheduled_departure
                         , scheduled_arrival
                         , scheduled_arrival - scheduled_departure AS duration
                    FROM bookings.flights5232
                    
                    WHERE status = 'Scheduled'
                    ORDER BY scheduled_departure
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/passengers", tags=['passengers'], response_model=list[Passenger])
def get_passengers(limit: int = Query(50, ge=1, le=1000),
                   page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT passenger_id
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
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/routes", tags=['routes'], response_model=list[Route])
def get_routes(limit: int = Query(50, ge=1, le=1000),
               page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT route_no
                         , concat(validity) AS validity
                         , departure_airport
                         , arrival_airport
                         , airplane_code
                         , days_of_week
                         , scheduled_time
                         , duration
                    FROM bookings.routes
                    ORDER BY route_no
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/segments", tags=['segments'], response_model=list[Segment])
def get_segments(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT DISTINCT flight_id
                                   ,fare_conditions
                                   ,price
                    FROM bookings.segments
                    ORDER BY price
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/seats", tags=['seats'], response_model=list[Seat])
def get_seats(limit: int = Query(50, ge=1, le=1000),
              page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT airplane_code
                         , seat_no
                         , fare_conditions
                    FROM bookings.seats
                    ORDER BY airplane_code, seat_no
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()


@router.get("/tickets", tags=['tickets'], response_model=list[Ticket])
def get_tickets(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    query = text("""SELECT ticket_no
                         , book_ref
                         , passenger_id
                         , passenger_name
                         , outbound
                    FROM bookings.tickets
                    ORDER BY ticket_no
                    LIMIT :limit OFFSET :offset""")
    with get_db_context() as session:
        result = session.execute(query, {'limit': limit, 'offset': offset})
        return result.mappings().all()

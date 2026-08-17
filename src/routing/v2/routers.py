from fastapi import APIRouter, Query
from src.docs import (airplane_docs, airports_docs, boarding_passes_docs,
                      bookings_docs, flights_docs, passengers_docs,
                      routes_docs, seats_docs, segments_docs, tickets_docs)
from src.schemas.schemas import (Airplane, Airport, BoardingPass, Booking, Flight,
                                 Route, Seat, Segment, Ticket, Passenger)
from src.services.services import (
    airplanes_service,
    airports_service,
    boarding_passes_service,
    bookings_service,
    flights_service,
    passengers_service,
    routes_service,
    segments_service,
    seats_service,
    tickets_service,
)

router = APIRouter(prefix="/v2", tags=['v2'])


@router.get(
    "/airplanes",
    response_model=list[Airplane],
    summary="Получить список самолётов",
    description=airplane_docs)
def get_airplanes(limit: int = Query(50, ge=1, le=1000),
                  page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return airplanes_service(limit=limit, offset=offset)


@router.get('/airports', response_model=list[Airport],
            summary='Получить список аэропортов',
            description=airports_docs)
def get_airports(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return airports_service(limit=limit, offset=offset)


@router.get('/bookings', response_model=list[Booking],
            summary='Получить список бронирований',
            description=bookings_docs)
def get_bookings(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return bookings_service(limit=limit, offset=offset)


@router.get('/boarding_passes', response_model=list[BoardingPass],
            summary='Получить список посадочных талонов',
            description=boarding_passes_docs)
def get_boarding_passes(limit: int = Query(50, ge=1, le=1000),
                        page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return boarding_passes_service(limit=limit, offset=offset)


@router.get('/flights', response_model=list[Flight],
            summary='Получить список полетов',
            description=flights_docs)
def get_flights(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return flights_service(limit=limit, offset=offset)


@router.get('/routes', response_model=list[Route],
            summary='Получить список маршрутов',
            description=routes_docs)
def get_routes(limit: int = Query(50, ge=1, le=1000),
               page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return routes_service(limit=limit, offset=offset)


@router.get('/seats', response_model=list[Seat],
            summary='Получить список посадочных мест',
            description=seats_docs)
def get_seats(limit: int = Query(50, ge=1, le=1000),
              page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return seats_service(limit=limit, offset=offset)


@router.get('/segments', response_model=list[Segment],
            summary='Получить список сегментов',
            description=segments_docs)
def get_segments(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return segments_service(limit=limit, offset=offset)


@router.get('/tickets', response_model=list[Ticket],
            summary='Получить список билетов',
            description=tickets_docs)
def get_tickets(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return tickets_service(limit=limit, offset=offset)


@router.get('/passengers', response_model=list[Passenger],
            summary='Получить список пассажиров',
            description=passengers_docs)
def get_passengers(limit: int = Query(50, ge=1, le=1000),
                   page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return passengers_service(limit=limit, offset=offset)

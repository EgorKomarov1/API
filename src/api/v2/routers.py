from fastapi import APIRouter, Query
from src.schemas import (Airplane, Airport, BoardingPass, Booking, Flight,
                         Route, Seat, Segment, Ticket, Passenger)
from src.services import (AirplaneService, AirportService, FlightService, PassengerService, SegmentService,
                          SeatService, TicketService, RouteService, BookingService, BoardingPassService)

router = APIRouter(prefix="/v2", tags=['v2'])

airplane_service = AirplaneService()
airport_service = AirportService()
boarding_pass_service = BoardingPassService()
booking_service = BookingService()
flight_service = FlightService()
passenger_service = PassengerService()
route_service = RouteService()
seat_service = SeatService()
segment_service = SegmentService()
ticket_service = TicketService()


@router.get('/airplanes', response_model=list[Airplane])
def get_airplanes(limit: int = Query(50, ge=1, le=1000),
                  page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return airplane_service.get_airplanes(limit=limit, offset=offset)


@router.get('/airports', response_model=list[Airport])
def get_airports(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return airport_service.get_airports(limit=limit, offset=offset)


@router.get('/bookings', response_model=list[Booking])
def get_bookings(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return booking_service.get_bookings(limit=limit, offset=offset)


@router.get('/boarding_passes', response_model=list[BoardingPass])
def get_boarding_passes(limit: int = Query(50, ge=1, le=1000),
                        page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return boarding_pass_service.get_boarding_passes(limit=limit, offset=offset)


@router.get('/flights', response_model=list[Flight])
def get_flights(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return flight_service.get_flights(limit=limit, offset=offset)


@router.get('/routes', response_model=list[Route])
def get_routes(limit: int = Query(50, ge=1, le=1000),
               page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return route_service.get_routes(limit=limit, offset=offset)


@router.get('/seats', response_model=list[Seat])
def get_seats(limit: int = Query(50, ge=1, le=1000),
              page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return seat_service.get_seats(limit=limit, offset=offset)


@router.get('/segments', response_model=list[Segment])
def get_segments(limit: int = Query(50, ge=1, le=1000),
                 page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return segment_service.get_segments(limit=limit, offset=offset)


@router.get('/tickets', response_model=list[Ticket])
def get_tickets(limit: int = Query(50, ge=1, le=1000),
                page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return ticket_service.get_tickets(limit=limit, offset=offset)


@router.get('/passengers', response_model=list[Passenger])
def get_passengers(limit: int = Query(50, ge=1, le=1000),
                   page: int = Query(1, ge=1)):
    offset = (page - 1) * limit
    return passenger_service.get_passengers(limit=limit, offset=offset)

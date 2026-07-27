
from typing import List, Dict, Any
from src.repositories import (AirportsRepository, AirplanesRepository, BookingsRepository, BoardingPassesRepository,
                              SeatsRepository, SegmentsRepository, TicketsRepository, RoutesRepository,
                              FlightsRepository, PassengersRepository)


class AirplaneService:
    def __init__(self):
        self.repository = AirplanesRepository()

    def get_airplanes(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_airplane_data(limit, offset)


class AirportService:
    def __init__(self):
        self.repository = AirportsRepository()

    def get_airports(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_airports_data(limit, offset)


class BoardingPassService:
    def __init__(self):
        self.repository = BoardingPassesRepository()

    def get_boarding_passes(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_boarding_passes(limit, offset)


class BookingService:
    def __init__(self):
        self.repository = BookingsRepository()

    def get_bookings(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_bookings(limit, offset)


class FlightService:
    def __init__(self):
        self.repository = FlightsRepository()

    def get_flights(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_flights(limit, offset)


class PassengerService:
    def __init__(self):
        self.repository = PassengersRepository()

    def get_passengers(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_passengers(limit, offset)


class RouteService:
    def __init__(self):
        self.repository = RoutesRepository()

    def get_routes(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_routes(limit, offset)


class SegmentService:
    def __init__(self):
        self.repository = SegmentsRepository()

    def get_segments(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_segments(limit, offset)


class SeatService:
    def __init__(self):
        self.repository = SeatsRepository()

    def get_seats(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_seats(limit, offset)


class TicketService:
    def __init__(self):
        self.repository = TicketsRepository()

    def get_tickets(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        return self.repository.get_tickets(limit, offset)

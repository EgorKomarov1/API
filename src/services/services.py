from typing import Any
from src.repositories import (
    get_airplane_data_repository,
    get_airports_data_repository,
    get_boarding_passes_repository,
    get_bookings_repository,
    get_flights_repository,
    get_passengers_repository,
    get_routes_repository,
    get_segments_repository,
    get_seats_repository,
    get_tickets_repository,
)


def airplanes_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_airplane_data_repository(limit, offset)


def airports_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_airports_data_repository(limit, offset)


def boarding_passes_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_boarding_passes_repository(limit, offset)


def bookings_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_bookings_repository(limit, offset)


def flights_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_flights_repository(limit, offset)


def passengers_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_passengers_repository(limit, offset)


def routes_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_routes_repository(limit, offset)


def segments_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_segments_repository(limit, offset)


def seats_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_seats_repository(limit, offset)


def tickets_service(limit: int = 50, offset: int = 0) -> list[dict[str, Any]]:
    return get_tickets_repository(limit, offset)

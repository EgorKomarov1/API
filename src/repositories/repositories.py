from src.database.db import engine
from src.sql_queries import (airplanes_query, airports_query, bookings_query, boarding_passes_query,
                             seats_query, segments_query, passengers_query, routes_query, flights_query,
                             tickets_query)


def get_airplane_data_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(airplanes_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_airports_data_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(airports_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_boarding_passes_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(boarding_passes_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_bookings_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(bookings_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_flights_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(flights_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_passengers_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(passengers_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_routes_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(routes_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_segments_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(segments_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_seats_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(seats_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_tickets_repository(limit: int = 50, offset: int = 0):
    with engine.begin() as conn:
        result = conn.execute(tickets_query, {"limit": limit, "offset": offset})
        return result.mappings().all()

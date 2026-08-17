from src.database.db import engine, get_sql
import pandas as pd


def get_airplanes_data_repository(limit: int = 50, offset: int = 0):
    airplanes_query = get_sql("select_airplanes.sql")
    with engine.begin() as conn:
        result = conn.execute(airplanes_query, {'limit': limit, 'offset': offset})
        return pd.DataFrame(result)


def get_airports_data_repository(limit: int = 50, offset: int = 0):
    airports_query = get_sql("select_airports.sql")
    with engine.begin() as conn:
        result = conn.execute(airports_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_boarding_passes_repository(limit: int = 50, offset: int = 0):
    boarding_passes_query = get_sql("select_boarding_passes.sql")
    with engine.begin() as conn:
        result = conn.execute(boarding_passes_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_bookings_repository(limit: int = 50, offset: int = 0):
    bookings_query = get_sql("select_bookings.sql")
    with engine.begin() as conn:
        result = conn.execute(bookings_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_flights_repository(limit: int = 50, offset: int = 0):
    flights_query = get_sql("select_flights.sql")
    with engine.begin() as conn:
        result = conn.execute(flights_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_passengers_repository(limit: int = 50, offset: int = 0):
    passengers_query = get_sql("select_passengers.sql")
    with engine.begin() as conn:
        result = conn.execute(passengers_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_routes_repository(limit: int = 50, offset: int = 0):
    routes_query = get_sql("select_routes.sql")
    with engine.begin() as conn:
        result = conn.execute(routes_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_segments_repository(limit: int = 50, offset: int = 0):
    segments_query = get_sql("select_segments.sql")
    with engine.begin() as conn:
        result = conn.execute(segments_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_seats_repository(limit: int = 50, offset: int = 0):
    seats_query = get_sql("select_seats.sql")
    with engine.begin() as conn:
        result = conn.execute(seats_query, {"limit": limit, "offset": offset})
        return result.mappings().all()


def get_tickets_repository(limit: int = 50, offset: int = 0):
    tickets_query = get_sql("select_tickets.sql")
    with engine.begin() as conn:
        result = conn.execute(tickets_query, {"limit": limit, "offset": offset})
        return result.mappings().all()

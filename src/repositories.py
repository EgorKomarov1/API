from sqlalchemy import text
from src.db import get_db_context


class BaseRepository:
    def __init__(self, table_name: str, schema: str = "bookings"):
        self.table_name = table_name
        self.schema = schema

    def _get_full_table_name(self) -> str:
        return f"{self.schema}.{self.table_name}"


class AirplanesRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name="airplanes_data")

    def get_airplane_data(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT airplane_code
                              , model
                              , range
                              , speed
                         FROM {self._get_full_table_name()}
                         ORDER BY range DESC
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class AirportsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='airports_data')

    def get_airports_data(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT airport_code
                              , airport_name
                              , city, country
                              , coordinates
                              , timezone
                         FROM {self._get_full_table_name()}
                         ORDER BY airport_code
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class BoardingPassesRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='boarding_passes')

    def get_boarding_passes(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT ticket_no
                              , flight_id
                              , seat_no
                              , boarding_no
                              , boarding_time
                         FROM {self._get_full_table_name()}
                         ORDER BY boarding_time
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class BookingsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='bookings')

    def get_bookings(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT book_ref
                              , book_date
                              , total_amount
                         FROM {self._get_full_table_name()}
                         ORDER BY book_date
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class FlightsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='flights')

    def get_flights(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT route_no
                              , scheduled_departure
                              , scheduled_arrival
                              , scheduled_arrival - scheduled_departure AS duration
                         FROM {self._get_full_table_name()}
                         WHERE status = 'Scheduled'
                         ORDER BY scheduled_departure
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class PassengersRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='passengers')

    def get_passengers(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT passenger_id
                              , passenger_name
                              , ticket_no
                              , flight_id
                              , fare_conditions
                              , book_ref
                              , price
                              , outbound
                         FROM {self._get_full_table_name()}
                         ORDER BY passenger_id
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class RoutesRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='routes')

    def get_routes(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT route_no
                              , concat(validity) AS validity
                              , departure_airport
                              , arrival_airport
                              , airplane_code
                              , days_of_week
                              , scheduled_time
                              , duration::text AS duration
                         FROM {self._get_full_table_name()}
                         ORDER BY route_no
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class SegmentsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='segments')

    def get_segments(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT DISTINCT flight_id
                                        ,fare_conditions
                                        ,price
                         FROM {self._get_full_table_name()}
                         ORDER BY price
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class SeatsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='seats')

    def get_seats(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT airplane_code
                              , seat_no
                              , fare_conditions
                         FROM {self._get_full_table_name()}
                         ORDER BY airplane_code, seat_no
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()


class TicketsRepository(BaseRepository):
    def __init__(self):
        super().__init__(table_name='tickets')

    def get_tickets(self, limit: int = 50, offset: int = 0):
        query = text(f"""SELECT ticket_no
                              , book_ref
                              , passenger_id
                              , passenger_name
                              , outbound
                         FROM {self._get_full_table_name()}
                         ORDER BY ticket_no
                         LIMIT :limit OFFSET :offset""")
        with get_db_context() as session:
            result = session.execute(query, {"limit": limit, "offset": offset})
            return result.mappings().all()

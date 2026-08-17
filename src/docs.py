airplane_docs = """
    Возвращает список всех самолётов с пагинацией.

    Пример ответа:
    [
        {
            "airplane_code": "PG001",
            "model": {"en": "Boeing 737", "ru": "Боинг 737"},
            "range": 5000,
            "speed": 800,
            "max_flight_time_hours": 6.5
        }
    ]
"""

airports_docs = """
    Возвращает список всех аэропортов с пагинацией.
    
    Пример ответа:
    [
        {
            "airport_code": "SVO",
            "airport_name": {"en": "Sheremetyevo", "ru": "Шереметьево"},
            "city": {"en": "Moscow", "ru": "Москва"},
            "country": {"en": "Russia", "ru": "Россия"},
            "coordinates": "55.9726, 37.4146",
            "timezone": "Europe/Moscow"
        }
    ]
"""

boarding_passes_docs = """
    Возвращает список всех посадочных талонов с пагинацией.
    
    Пример ответа:
    [
        {
            "ticket_no": "123",
            "flight_id": 100,
            "seat_no": "12A",
            "boarding_no": 1,
            "boarding_time": "2026-01-01T10:00:00"
        }
    ]
"""

bookings_docs = """
    Возвращает список всех бронирований с пагинацией.
    
    Пример ответа:
    [
        {
            "book_ref": "BOOK123",
            "book_date": "2026-01-01T10:00:00",
            "total_amount": 1500.50
        }
    ]
"""

flights_docs = """
    Возвращает список всех запланированных рейсов с пагинацией.
    
    Пример ответа:
    [
        {
            "route_no": "PG123",
            "scheduled_departure": "2026-01-01T10:00:00",
            "scheduled_arrival": "2026-01-01T12:00:00",
            "duration": "02:00:00"
        }
    ]
"""

passengers_docs = """
    Возвращает список всех пассажиров с пагинацией.
    
    Пример ответа:
    [
        {
            "passenger_id": "PASS123",
            "passenger_name": "John",
            "ticket_no": "TICKET123",
            "flight_id": 100,
            "fare_conditions": "Economy",
            "book_ref": "BOOK123",
            "price": 500.00,
            "outbound": true
        }
    ]
"""

routes_docs = """
    Возвращает список всех маршрутов с пагинацией.
    
    Пример ответа:
    [
        {
            "route_no": "PG123",
            "validity": "[2026-01-01,2026-12-31)",
            "departure_airport": "AAA",
            "arrival_airport": "LED",
            "airplane_code": "PG001",
            "days_of_week": [1, 3, 5],
            "scheduled_time": "10:00:00",
            "duration": "02:00:00"
        }
    ]
"""

seats_docs = """
    Возвращает список всех мест в самолётах с пагинацией.
    
    Пример ответа:
    [
        {
            "airplane_code": "PG001",
            "seat_no": "12A",
            "fare_conditions": "Economy"
        }
    ]
"""

segments_docs = """
    Возвращает список всех сегментов перелётов с пагинацией.
    
    Пример ответа:
    [
        {
            "flight_id": 100,
            "fare_conditions": "Economy",
            "price": 500.00
        }
    ]
"""

tickets_docs = """
    Возвращает список всех билетов с пагинацией.
    
    Пример ответа:
    [
        {
            "ticket_no": "123",
            "book_ref": "BOOK123",
            "passenger_id": "PASS123",
            "passenger_name": "John",
            "outbound": true
        }
    ]
"""
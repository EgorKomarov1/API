from src.services import (
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


def test_airplanes_service():
    limit = 5
    offset = 0
    result = airplanes_service(limit, offset)

    assert isinstance(result, list)
    if result:
        assert 'airplane_code' in result[0]


def test_airports_service():
    result = airports_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_boarding_passes_service():
    result = boarding_passes_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_bookings_service():
    result = bookings_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_flights_service():
    result = flights_service(limit=5, offset=0)
    assert isinstance(result, list)
    if result:
        assert 'route_no' in result[0]


def test_passengers_service():
    result = passengers_service(limit=5, offset=0)
    assert isinstance(result, list)
    if result:
        assert 'passenger_name' in result[0]


def test_routes_service():
    result = routes_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_segments_service():
    result = segments_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_seats_service():
    result = seats_service(limit=5, offset=0)
    assert isinstance(result, list)


def test_tickets_service():
    result = tickets_service(limit=5, offset=0)
    assert isinstance(result, list)
    if result:
        assert 'ticket_no' in result[0]

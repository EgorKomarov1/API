# tests/test_repositories.py
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


def test_airplanes_repository():
    limit = 5
    offset = 0
    result = get_airplane_data_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'airplane_code' in item
        assert 'model' in item
        assert 'range' in item
        assert 'speed' in item


def test_airports_repository():
    limit = 5
    offset = 0
    result = get_airports_data_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'airport_code' in item
        assert 'airport_name' in item
        assert 'city' in item
        assert 'country' in item
        assert 'coordinates' in item
        assert 'timezone' in item


def test_boarding_passes_repository():
    limit = 5
    offset = 0
    result = get_boarding_passes_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'ticket_no' in item
        assert 'flight_id' in item
        assert 'seat_no' in item
        assert 'boarding_no' in item
        assert 'boarding_time' in item


def test_bookings_repository():
    limit = 5
    offset = 0
    result = get_bookings_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'book_ref' in item
        assert 'book_date' in item
        assert 'total_amount' in item


def test_flights_repository():
    limit = 5
    offset = 0
    result = get_flights_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'route_no' in item
        assert 'scheduled_departure' in item
        assert 'scheduled_arrival' in item
        assert 'duration' in item


def test_passengers_repository():
    limit = 5
    offset = 0
    result = get_passengers_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'passenger_id' in item
        assert 'passenger_name' in item
        assert 'ticket_no' in item
        assert 'flight_id' in item
        assert 'fare_conditions' in item
        assert 'book_ref' in item
        assert 'price' in item
        assert 'outbound' in item


def test_routes_repository():
    limit = 5
    offset = 0
    result = get_routes_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'route_no' in item
        assert 'validity' in item
        assert 'departure_airport' in item
        assert 'arrival_airport' in item
        assert 'airplane_code' in item
        assert 'days_of_week' in item
        assert 'scheduled_time' in item
        assert 'duration' in item


def test_segments_repository():
    limit = 5
    offset = 0
    result = get_segments_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'flight_id' in item
        assert 'fare_conditions' in item
        assert 'price' in item


def test_seats_repository():
    limit = 5
    offset = 0
    result = get_seats_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'airplane_code' in item
        assert 'seat_no' in item
        assert 'fare_conditions' in item


def test_tickets_repository():
    limit = 5
    offset = 0
    result = get_tickets_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        item = result[0]
        assert 'ticket_no' in item
        assert 'book_ref' in item
        assert 'passenger_id' in item
        assert 'passenger_name' in item
        assert 'outbound' in item

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
        assert 'airplane_code' in result[0]
        assert 'model' in result[0]
        assert 'range' in result[0]


def test_airports_repository():
    limit = 5
    offset = 0
    result = get_airports_data_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'airport_code' in result[0]
        assert 'airport_name' in result[0]
        assert 'city' in result[0]


def test_boarding_passes_repository():
    limit = 5
    offset = 0
    result = get_boarding_passes_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'ticket_no' in result[0]
        assert 'flight_id' in result[0]
        assert 'seat_no' in result[0]


def test_bookings_repository():
    limit = 5
    offset = 0
    result = get_bookings_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'book_ref' in result[0]
        assert 'book_date' in result[0]
        assert 'total_amount' in result[0]


def test_flights_repository():
    limit = 5
    offset = 0
    result = get_flights_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'route_no' in result[0]
        assert 'scheduled_departure' in result[0]
        assert 'scheduled_arrival' in result[0]


def test_passengers_repository():
    limit = 5
    offset = 0
    result = get_passengers_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'passenger_id' in result[0]
        assert 'passenger_name' in result[0]
        assert 'ticket_no' in result[0]


def test_routes_repository():
    limit = 5
    offset = 0
    result = get_routes_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'route_no' in result[0]
        assert 'departure_airport' in result[0]
        assert 'arrival_airport' in result[0]


def test_segments_repository():
    limit = 5
    offset = 0
    result = get_segments_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'flight_id' in result[0]
        assert 'fare_conditions' in result[0]
        assert 'price' in result[0]


def test_seats_repository():
    limit = 5
    offset = 0
    result = get_seats_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'airplane_code' in result[0]
        assert 'seat_no' in result[0]
        assert 'fare_conditions' in result[0]


def test_tickets_repository():
    limit = 5
    offset = 0
    result = get_tickets_repository(limit, offset)

    assert isinstance(result, list)
    assert len(result) <= limit
    if result:
        assert 'ticket_no' in result[0]
        assert 'book_ref' in result[0]
        assert 'passenger_name' in result[0]
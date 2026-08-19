from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app

client = TestClient(app)


def test_airplanes_router():
    mock_data = [
        {"airplane_code": "PG001",
         "model": {"en": "Boeing 737"},
         "range": 5000,
         "speed": 800,
         "max_flight_time_hours": 2.5
         }
    ]

    with patch('src.routing.v2.routers.airplanes_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/airplanes?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["airplane_code"] == "PG001"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_airports_router():
    mock_data = [
        {
            "airport_code": "AAA",
            "airport_name": {"en": "Domodedovo"},
            "city": {"en": "Moscow"},
            "country": {"en": "Russia"},
            "coordinates": "55.9726, 37.4146",
            "timezone": "Europe/Moscow"
        }
    ]

    with patch('src.routing.v2.routers.airports_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/airports?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["airport_code"] == "AAA"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_boarding_passes_router():
    mock_data = [
        {
            "ticket_no": "123",
            "flight_id": 100,
            "seat_no": "12A",
            "boarding_no": 1,
            "boarding_time": "2026-01-01T10:00:00"
        }
    ]

    with patch('src.routing.v2.routers.boarding_passes_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/boarding_passes?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["ticket_no"] == "123"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_bookings_router():
    mock_data = [
        {
            "book_ref": "123",
            "book_date": "2026-01-01T10:00:00",
            "total_amount": 1500.50
        }
    ]

    with patch('src.routing.v2.routers.bookings_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/bookings?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["book_ref"] == "123"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_flights_router():
    mock_data = [
        {
            "route_no": "PG123",
            "scheduled_departure": "2026-01-01T10:00:00",
            "scheduled_arrival": "2026-01-01T12:00:00",
            "duration": "02:00:00"
        }
    ]

    with patch('src.routing.v2.routers.flights_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/flights?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["route_no"] == "PG123"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_passengers_router():
    mock_data = [
        {
            "passenger_id": "123",
            "passenger_name": "John",
            "ticket_no": "123",
            "flight_id": 100,
            "fare_conditions": "Economy",
            "book_ref": "123",
            "price": 500.00,
            "outbound": True
        }
    ]

    with patch('src.routing.v2.routers.passengers_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/passengers?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["passenger_name"] == "John"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_routes_router():
    mock_data = [
        {
            "route_no": "PG123",
            "validity": "[2026-01-01,2026-12-31)",
            "departure_airport": "AAA",
            "arrival_airport": "BBB",
            "airplane_code": "PG001",
            "days_of_week": [1, 3, 5],
            "scheduled_time": "10:00:00",
            "duration": "02:00:00"
        }
    ]

    with patch('src.routing.v2.routers.routes_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/routes?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["route_no"] == "PG123"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_segments_router():
    mock_data = [
        {
            "flight_id": 100,
            "fare_conditions": "Economy",
            "price": 500.00
        }
    ]

    with patch('src.routing.v2.routers.segments_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/segments?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["flight_id"] == 100
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_seats_router():
    mock_data = [
        {
            "airplane_code": "PG001",
            "seat_no": "12A",
            "fare_conditions": "Economy"
        }
    ]

    with patch('src.routing.v2.routers.seats_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/seats?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["seat_no"] == "12A"
        mock_service.assert_called_once_with(limit=5, offset=0)


def test_tickets_router():
    mock_data = [
        {
            "ticket_no": "123",
            "book_ref": "123",
            "passenger_id": "123",
            "passenger_name": "John",
            "outbound": True
        }
    ]

    with patch('src.routing.v2.routers.tickets_service') as mock_service:
        mock_service.return_value = mock_data

        response = client.get("/v2/tickets?limit=5&page=1")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["ticket_no"] == "123"
        mock_service.assert_called_once_with(limit=5, offset=0)

from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_get_airplanes():
    response = client.get("/v2/airplanes?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "airplane_code" in data[0]
        assert "model" in data[0]


def test_get_airports():
    response = client.get("/v2/airports?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "airport_code" in data[0]
        assert "airport_name" in data[0]


def test_get_boarding_passes():
    response = client.get("/v2/boarding_passes?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "ticket_no" in data[0]
        assert "flight_id" in data[0]


def test_get_bookings():
    response = client.get("/v2/bookings?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "book_ref" in data[0]
        assert "book_date" in data[0]


def test_get_flights():
    response = client.get("/v2/flights?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "route_no" in data[0]
        assert "scheduled_departure" in data[0]


def test_get_passengers():
    response = client.get("/v2/passengers?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "passenger_id" in data[0]
        assert "passenger_name" in data[0]


def test_get_routes():
    response = client.get("/v2/routes?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "route_no" in data[0]
        assert "departure_airport" in data[0]


def test_get_segments():
    response = client.get("/v2/segments?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "flight_id" in data[0]
        assert "price" in data[0]


def test_get_seats():
    response = client.get("/v2/seats?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "airplane_code" in data[0]
        assert "seat_no" in data[0]


def test_get_tickets():
    response = client.get("/v2/tickets?limit=5&page=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "ticket_no" in data[0]
        assert "passenger_name" in data[0]

from unittest.mock import patch
from src.services.services import (
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
import pandas as pd


def test_airplanes_service():
    mock_data = pd.DataFrame([
        {
            'airplane_code': 'PG001',
            'model': {'en': 'Boeing 737'},
            'range': 5000,
            'speed': 800
        }
    ])

    with patch('src.services.services.get_airplanes_data_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = airplanes_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['airplane_code'] == 'PG001'
        assert result[0]['model']['en'] == 'Boeing 737'
        mock_repo.assert_called_once_with(5, 0)


def test_airports_service():
    mock_data = [
        {
            'airport_code': 'AAA',
            'airport_name': {'en': 'Domodedovo'},
            'city': {'en': 'Moscow'},
            'country': {'en': 'Russia'},
            'coordinates': '55.9726, 37.4146',
            'timezone': 'Moscow'
        }
    ]

    with patch('src.services.services.get_airports_data_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = airports_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['airport_code'] == 'AAA'
        mock_repo.assert_called_once_with(5, 0)


def test_boarding_passes_service():
    mock_data = [
        {
            'ticket_no': '123',
            'flight_id': 100,
            'seat_no': '12A',
            'boarding_no': 1,
            'boarding_time': '2026-01-01T10:00:00'
        }
    ]

    with patch('src.services.services.get_boarding_passes_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = boarding_passes_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['ticket_no'] == '123'
        mock_repo.assert_called_once_with(5, 0)


def test_bookings_service():
    mock_data = [
        {
            'book_ref': '123',
            'book_date': '2026-01-01T10:00:00',
            'total_amount': 1500.50
        }
    ]

    with patch('src.services.services.get_bookings_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = bookings_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['book_ref'] == '123'
        mock_repo.assert_called_once_with(5, 0)


def test_flights_service():
    mock_data = [
        {
            'route_no': 'PG123',
            'scheduled_departure': '2026-01-01T10:00:00',
            'scheduled_arrival': '2026-01-01T12:00:00',
            'duration': '02:00:00'
        }
    ]

    with patch('src.services.services.get_flights_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = flights_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['route_no'] == 'PG123'
        mock_repo.assert_called_once_with(5, 0)


def test_passengers_service():
    mock_data = [
        {
            'passenger_id': '123',
            'passenger_name': 'John Smith',
            'ticket_no': '123',
            'flight_id': 100,
            'fare_conditions': 'Economy',
            'book_ref': 'BOOK123',
            'price': 500.00,
            'outbound': True
        }
    ]

    with patch('src.services.services.get_passengers_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = passengers_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['passenger_name'] == 'John Smith'
        mock_repo.assert_called_once_with(5, 0)


def test_routes_service():
    mock_data = [
        {
            'route_no': 'PG123',
            'validity': '[2026-01-01,2026-12-31)',
            'departure_airport': 'AAA',
            'arrival_airport': 'BBB',
            'airplane_code': 'PG001',
            'days_of_week': [1, 3, 5],
            'scheduled_time': '10:00:00',
            'duration': '02:00:00'
        }
    ]

    with patch('src.services.services.get_routes_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = routes_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['route_no'] == 'PG123'
        mock_repo.assert_called_once_with(5, 0)


def test_segments_service():
    mock_data = [
        {
            'flight_id': 100,
            'fare_conditions': 'Economy',
            'price': 500.00
        }
    ]

    with patch('src.services.services.get_segments_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = segments_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['flight_id'] == 100
        mock_repo.assert_called_once_with(5, 0)


def test_seats_service():
    mock_data = [
        {
            'airplane_code': 'PG001',
            'seat_no': '12A',
            'fare_conditions': 'Economy'
        }
    ]

    with patch('src.services.services.get_seats_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = seats_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['seat_no'] == '12A'
        mock_repo.assert_called_once_with(5, 0)


def test_tickets_service():
    mock_data = [
        {
            'ticket_no': '123',
            'book_ref': '123',
            'passenger_id': '123',
            'passenger_name': 'John Smith',
            'outbound': True
        }
    ]

    with patch('src.services.services.get_tickets_repository') as mock_repo:
        mock_repo.return_value = mock_data

        result = tickets_service(limit=5, offset=0)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]['ticket_no'] == '123'
        mock_repo.assert_called_once_with(5, 0)

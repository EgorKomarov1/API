from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional, List
from decimal import Decimal


class Airplane(BaseModel):
    airplane_code: str
    model: dict
    range: int
    speed: Optional[int]
    max_flight_time_hours: float


class Airport(BaseModel):
    airport_code: str
    airport_name: dict
    city: dict
    country: dict
    coordinates: Optional[str]
    timezone: Optional[str]


class BoardingPass(BaseModel):
    ticket_no: str
    flight_id: int
    seat_no: str
    boarding_no: Optional[int]
    boarding_time: Optional[datetime]


class Booking(BaseModel):
    book_ref: str
    book_date: datetime
    total_amount: Decimal


class Flight(BaseModel):
    route_no: str
    scheduled_departure: datetime
    scheduled_arrival: datetime


class Route(BaseModel):
    route_no: str
    validity: Optional[str]
    departure_airport: str
    arrival_airport: str
    airplane_code: str
    days_of_week: List[int]
    scheduled_time: time
    duration: Optional[str]


class Seat(BaseModel):
    airplane_code: str
    seat_no: str
    fare_conditions: str


class Segment(BaseModel):
    flight_id: int
    fare_conditions: str
    price: Decimal


class Ticket(BaseModel):
    ticket_no: str
    book_ref: str
    passenger_id: str
    passenger_name: str
    outbound: bool


class Passenger(BaseModel):
    passenger_id: str
    passenger_name: str
    ticket_no: str
    flight_id: int
    fare_conditions: str
    book_ref: str
    price: Decimal
    outbound: bool

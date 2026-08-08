SELECT airplane_code
     , seat_no
     , fare_conditions
FROM bookings.seats
ORDER BY airplane_code, seat_no
LIMIT :limit OFFSET :offset
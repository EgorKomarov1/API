SELECT ticket_no
     , flight_id
     , seat_no
     , boarding_no
     , boarding_time
FROM bookings.boarding_passes
ORDER BY boarding_time
LIMIT :limit OFFSET :offset
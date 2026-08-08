SELECT passenger_id
     , passenger_name
     , ticket_no
     , flight_id
     , fare_conditions
     , book_ref
     , price
     , outbound
FROM bookings.passengers
ORDER BY passenger_id
LIMIT :limit OFFSET :offset
SELECT route_no
     , concat(validity) AS validity
     , departure_airport
     , arrival_airport
     , airplane_code
     , days_of_week
     , scheduled_time
     , duration::text AS duration
FROM bookings.routes
ORDER BY route_no
LIMIT :limit OFFSET :offset
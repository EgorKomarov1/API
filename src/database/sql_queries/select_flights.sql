SELECT route_no
     , scheduled_departure
     , scheduled_arrival
     , scheduled_arrival - scheduled_departure AS duration
FROM bookings.flights
WHERE status = 'Scheduled'
ORDER BY scheduled_departure
LIMIT :limit OFFSET :offset
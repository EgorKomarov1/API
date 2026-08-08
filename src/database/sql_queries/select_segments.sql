SELECT DISTINCT flight_id
               ,fare_conditions
               ,price
FROM bookings.segments
ORDER BY price
LIMIT :limit OFFSET :offset
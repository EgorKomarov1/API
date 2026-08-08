SELECT airport_code
     , airport_name
     , city, country
     , coordinates
     , timezone
FROM bookings.airports_data
ORDER BY airport_code
LIMIT :limit OFFSET :offset
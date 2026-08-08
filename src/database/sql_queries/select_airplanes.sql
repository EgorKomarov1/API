SELECT airplane_code
     , model
     , range
     , speed
FROM bookings.airplanes_data
ORDER BY range DESC
LIMIT :limit OFFSET :offset
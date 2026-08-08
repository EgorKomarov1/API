SELECT ticket_no
     , book_ref
     , passenger_id
     , passenger_name
     , outbound
FROM bookings.tickets
ORDER BY ticket_no
LIMIT :limit OFFSET :offset
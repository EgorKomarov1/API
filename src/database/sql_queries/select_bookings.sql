SELECT book_ref
     , book_date
     , total_amount
FROM bookings.bookings
ORDER BY book_date
LIMIT :limit OFFSET :offset
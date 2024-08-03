There is a function in Langchain that work with sql already:
    - It has a default sql prompt (but you can create your own custom prompt, I will try this)
    - https://python.langchain.com/v0.2/docs/tutorials/sql_qa/.
        - https://api.python.langchain.com/en/latest/chains/langchain.chains.sql_database.query.create_sql_query_chain.html, definition of a function used.
    - https://python.langchain.com/v0.2/docs/how_to/#use-cases, list of use cases, read it.


SELECT
tt.ticket_type_id,
tt.ticket_type_name,
SUM(bd.quantity) AS total_sold
FROM TicketType AS tt
JOIN BookingDetail AS bd
ON tt.ticket_type_id = bd.ticket_type_id
JOIN Booking AS b
ON bd.booking_id = b.booking_id
WHERE
b.created_at >= DATE_FORMAT(NOW(), '%Y-01-01')
GROUP BY
tt.ticket_type_id,
tt.ticket_type_name
ORDER BY
total_sold DESC
LIMIT 50;

I need >3.10

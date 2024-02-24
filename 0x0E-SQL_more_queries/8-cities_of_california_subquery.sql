-- List all the cities of California from the database hbtn_0d_usa
SELECT cities.*
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;

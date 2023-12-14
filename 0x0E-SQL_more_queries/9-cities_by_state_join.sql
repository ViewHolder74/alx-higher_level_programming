-- This script lists all cities contained in the database hbtn_0d_usa
-- Each record display: cities.id - cities.name - states.name
-- Results is sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

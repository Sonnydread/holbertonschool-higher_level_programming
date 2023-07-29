-- lists all cities contained in the hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name AS name FROM cities
JOIN states ON state_id = states.id ORDER BY cities.id ASC

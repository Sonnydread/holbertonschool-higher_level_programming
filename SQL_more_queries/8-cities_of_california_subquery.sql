-- list all the cities of California inside the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id=1 ORDER BY id ASC;

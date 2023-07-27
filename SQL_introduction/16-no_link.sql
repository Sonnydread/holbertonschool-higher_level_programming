-- list all records of second_table of hbtn_0c_0
-- results should display the score and the name (in this order)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

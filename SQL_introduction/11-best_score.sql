-- list all records with score >=10 inside second_table of hbtn_0c_0
-- records should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score>=10 ORDER BY score DESC

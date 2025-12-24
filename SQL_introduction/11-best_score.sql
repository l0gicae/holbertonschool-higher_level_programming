-- lists records with score >= 10 in second_table ordered by score (highest first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

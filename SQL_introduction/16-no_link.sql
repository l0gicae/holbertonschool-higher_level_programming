-- lists all records of second_table with a non-empty name, ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

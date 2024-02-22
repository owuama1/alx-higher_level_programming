/*
Script: List Records of second_table
Description: This script lists all records of the table second_table, excluding rows without a name value, and orders them by descending score.
*/

-- SQL: Select score and name from the table second_table where name is not null, ordered by score (descending)
SELECT score, name
FROM `second_table`
WHERE name IS NOT NULL
ORDER BY score DESC;

/*
Script: List Records with Score >= 10
Description: This script lists all records with a score greater than or equal to 10 in the table second_table of the database hbtn_0c_0, displaying both the score and the name, and ordering the records by score in descending order.
*/

-- SQL: Select score and name from the table second_table where score is greater than or equal to 10, ordered by score (top first)
SELECT score, name
FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;

/*
Script: List Number of Records with Same Score
Description: This script lists the number of records with the same score in the table second_table.
*/

-- SQL: Select score and count of records with the same score, ordered by count (descending)
SELECT score, COUNT(*) AS number
FROM `second_table`
GROUP BY score
ORDER BY number DESC;

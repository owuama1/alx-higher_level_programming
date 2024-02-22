/*
Script: List Records of second_table
Description: This script lists all records of the table second_table of the database hbtn_0c_0, displaying both the score and the name, and ordering the records by score in descending order.
*/

-- SQL: Select score and name from the table second_table, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
ORDER BY score DESC;

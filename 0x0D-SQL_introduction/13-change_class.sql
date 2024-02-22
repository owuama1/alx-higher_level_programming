/*
Script: Remove Records with Score <= 5
Description: This script removes all records with a score less than or equal to 5 in the table second_table.
*/

-- SQL: Delete records with score <= 5
DELETE FROM `second_table`
WHERE score <= 5;

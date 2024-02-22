/*
Script: Create Table first_table
Description: This script creates a table called first_table in the current database.
             If the table already exists, it won't cause any failure.
*/
-- SQL: Create table first_table with id INT and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);

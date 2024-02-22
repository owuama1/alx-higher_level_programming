/*
Script: Create and Populate second_table
Description: This script creates a table called second_table in the database hbtn_0c_0 and adds multiple rows to it.
*/

-- SQL: Create table second_table with id INT, name VARCHAR(256), and score INT
CREATE TABLE IF NOT EXISTS `second_table` (
	id INT,
	name VARCHAR(256),
	score INT
);

-- SQL: Insert multiple rows into the table second_table
INSERT INTO `second_table` (id, name, score)
VALUES 
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);

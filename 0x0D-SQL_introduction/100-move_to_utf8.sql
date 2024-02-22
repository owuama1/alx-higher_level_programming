/*
Script: Convert Database and Table to UTF8
Description: This script converts the hbtn_0c_0 database, the first_table table, and the name field in the first_table table to UTF8 (utf8mb4).
*/

-- SQL: Convert table first_table to UTF8
USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

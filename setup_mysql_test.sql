-- Cohort 6 is sooo goood
-- Script that sets up the MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates the new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

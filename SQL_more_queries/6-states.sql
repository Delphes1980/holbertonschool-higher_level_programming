-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on my MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;  -- allows you to use the DataBase you've created
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

-- create a database hbtn_0d_usa and the table cities
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(id INT AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY states (state_id) REFERENCES states(id));

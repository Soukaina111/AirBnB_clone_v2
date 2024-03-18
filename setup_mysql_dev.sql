-- if it does not exist create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- if it does not exist create User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- This line used to grant all privileges on the hbnb_dev_db to database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--This one is to  grant SELECT privilege on performance_schema to db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

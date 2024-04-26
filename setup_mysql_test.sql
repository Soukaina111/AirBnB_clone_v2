--  if it does not exist create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--  if it does not exist create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- This line grant all privileges on the hbnb_test_db to db_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- This line Grant SELECT privilege on performance_schema to db_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

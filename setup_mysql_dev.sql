-- script to create a database, create a user in localhost
-- grant privileges to him, flush the table privileges
-- to make effect, and use the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performarce_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
USE hbnb_test_db;

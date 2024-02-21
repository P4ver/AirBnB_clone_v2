-- Crt database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Crt user hbnb_dev if it doesn't exist, and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- all privileges on hbnb_dev_db to user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- SELECT privilege on performance_schema to user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- script that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or update hbnb_dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to hbnb_dev on hbnb_dev_db
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
-- This script creates the MySQL server user user_0d_1
-- user_0d_1 have all privileges on MySQL server
-- The user_0d_1 password is user_0d_1_pwd
-- if user user_0d_1 already exists, the script not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

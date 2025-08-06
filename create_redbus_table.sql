-- Run in MySQL
CREATE DATABASE IF NOT EXISTS redbus_data;
USE redbus_data;

CREATE TABLE IF NOT EXISTS bus_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Route_name VARCHAR(255),
    Route_link TEXT,
    Bus_Name VARCHAR(255),
    Bus_Type VARCHAR(100),
    Departing_Time TIME,
    Duration VARCHAR(50),
    Reaching_Time TIME,
    Star_Rating FLOAT,
    Price FLOAT,
    Seats_available INT
);

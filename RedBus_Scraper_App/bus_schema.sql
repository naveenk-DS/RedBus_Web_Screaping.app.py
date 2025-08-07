-- Create database if not exists
CREATE DATABASE IF NOT EXISTS redbus_data;

-- Switch to the database
USE redbus_data;

-- Create the bus_routes table
CREATE TABLE IF NOT EXISTS bus_routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_name TEXT,
    route_link TEXT,
    busname TEXT,
    bustype TEXT,
    departing_time TIME,
    duration TEXT,
    reaching_time TIME,
    star_rating FLOAT,
    price DECIMAL(10,2),
    seats_available INT
);

-- Create Database
CREATE DATABASE SalesDB;

USE SalesDB;

-- Create Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Region VARCHAR(50),
    City VARCHAR(50)
);

-- Insert Sample Data
INSERT INTO Customers VALUES
(1, 'Arun', 'South', 'Chennai'),
(2, 'Meera', 'West', 'Mumbai'),
(3, 'Rahul', 'North', 'Delhi');

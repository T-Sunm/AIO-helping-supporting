drop database if exists shoppingdb;
create database shoppingdb;

use shoppingdb;
CREATE TABLE Category (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Status BOOLEAN
);

CREATE TABLE Product (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Status BOOLEAN,
    Price FLOAT,
    SalePrice FLOAT,
    CreatedDate DATE,
    CategoryId INT,
    FOREIGN KEY (CategoryId)
        REFERENCES Category (Id),
    INDEX idx_product_name (Name)
);

CREATE TABLE Customer (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Email VARCHAR(150),
    Phone VARCHAR(50),
    Address VARCHAR(255),
    CreatedDate DATE,
    Gender BOOLEAN,
    BirthDay DATE
);

CREATE TABLE Orders (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    CustomerId INT NOT NULL,
    Status BOOLEAN,
    OrderDate DATETIME,
    FOREIGN KEY (CustomerId)
        REFERENCES Customer (Id)
);

CREATE TABLE OrderDetail (
    OrderId INT NOT NULL ,
    ProductId INT NOT NULL,
    Quantity INT NOT NULL,
    Price FLOAT NOT NULL,
    PRIMARY KEY (OrderId , ProductId),
    FOREIGN KEY (OrderId)
        REFERENCES Orders (Id),
    FOREIGN KEY (ProductId)
        REFERENCES Product (Id)
);

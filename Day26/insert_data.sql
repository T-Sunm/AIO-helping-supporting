USE shoppingdb;
INSERT INTO Category (Name, Status) VALUES
('Men Clothing', TRUE),
('Women Clothing', TRUE),
('Kids Clothing', TRUE),
('Accessories', TRUE),
('Footwear', TRUE);
INSERT INTO Product (Name, Status, Price, SalePrice, CreatedDate, CategoryId) VALUES
('Men T-Shirt', TRUE, 19.99, 14.99, '2024-07-01', 1),
('Men Jeans', TRUE, 49.99, 39.99, '2024-07-02', 1),
('Women Dress', TRUE, 69.99, 59.99, '2024-07-03', 2),
('Women Skirt', TRUE, 29.99, 24.99, '2024-07-04', 2),
('Kids T-Shirt', TRUE, 15.99, 12.99, '2024-07-05', 3),
('Kids Shorts', TRUE, 25.99, 20.99, '2024-07-06', 3),
('Sunglasses', TRUE, 89.99, 79.99, '2024-07-07', 4),
('Hat', TRUE, 15.99, 10.99, '2024-07-08', 4),
('Sneakers', TRUE, 129.99, 99.99, '2024-07-09', 5),
('Sandals', TRUE, 29.99, 19.99, '2024-07-10', 5),
('Men Jacket', TRUE, 99.99, 79.99, '2024-07-11', 1),
('Women Blouse', TRUE, 39.99, 34.99, '2024-07-12', 2),
('Kids Jacket', TRUE, 45.99, 35.99, '2024-07-13', 3),
('Belt', TRUE, 20.99, 15.99, '2024-07-14', 4),
('Boots', TRUE, 149.99, 129.99, '2024-07-15', 5);
INSERT INTO Customer (Name, Email, Phone, Address, CreatedDate, Gender, BirthDay) VALUES
('John Doe', 'john.doe@example.com', '1234567890', '123 Elm St', '2024-07-01', TRUE, '1990-05-15'),
('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Oak St', '2024-07-02', FALSE, '1985-08-25'),
('Alice Johnson', 'alice.johnson@example.com', '1122334455', '789 Pine St', '2024-07-03', FALSE, '1992-11-30');
INSERT INTO Orders (CustomerId, Status, OrderDate) VALUES
(1, TRUE, '2024-07-15 10:00:00'),
(2, TRUE, '2024-07-16 11:00:00'),
(3, TRUE, '2024-07-17 12:00:00');
INSERT INTO OrderDetail (OrderId, ProductId, Quantity, Price) VALUES
(1, 1, 2, 14.99),
(1, 2, 1, 39.99),
(2, 3, 1, 59.99),
(2, 4, 2, 24.99),
(3, 5, 1, 12.99),
(3, 6, 3, 20.99);

		
USE shoppingdb;

-- CÂU 1
-- SELECT * FROM Product
-- ORDER BY Price DESC;

-- CÂU 2 
-- SELECT 
-- 	Category.Id,
--     Category.Name,
--     COUNT(Product.Name) AS NumberOfProducts,
--     Category.Status
-- FROM
--     Category
-- JOIN 
--     Product ON Category.Id = Product.CategoryId
-- GROUP BY 
--     Category.Id;

-- CÂU 3
 select 
	Id, Name, Email, Phone, Address, CreatedDate, 
    if(Gender = 0, 'Nữ', 'Nam') as Gender ,
    BirthDay, 
	timestampdiff(YEAR, BirthDay, curdate()) as Age
 from customer
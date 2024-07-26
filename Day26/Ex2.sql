Use shoppingdb;
SELECT 
	Category.Id,
    Category.Name,
    COUNT(Product.Name) AS TotalProduct,
    Category.Status
FROM
    Category
JOIN 
    Product ON Category.Id = Product.CategoryId
GROUP BY 
    Category.Id;
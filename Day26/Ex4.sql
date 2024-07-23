Use shoppingdb;
SET SQL_SAFE_UPDATES = 0;
delete 
    p
FROM
    Product p
        LEFT JOIN
    OrderDetail od ON od.ProductId = p.Id
WHERE
    od.OrderId IS NULL
;
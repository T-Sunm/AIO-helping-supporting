
Use shoppingdb;

update product as p
set p.SalePrice = p.SalePrice * (1 + 10/100)
where p.SalePrice <= 250000
;
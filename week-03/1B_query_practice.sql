USE northwind; 
SELECT productid, productname, unitprice 
FROM products;
SELECT productid, productName, unitprice 
FROM products
WHERE unitprice < 7.50;
SELECT productid, productName, unitprice
FROM products
WHERE unitsinstock = 0
AND unitsonorder >0;
-- grogonzola telino 
SELECT productName, unitprice
FROM products
JOIN categories 
ON products.CategoryID = categories.CategoryID
WHERE categoryName = 'seafood';
SELECT supplierid, companyName
FROM suppliers
WHERE companyName = 'tokyo traders';
SELECT COUNT(*) AS totalemployess
FROM employees;
SELECT firstName, lastName, title 
FROM employees
WHERE title LIKE '%manager%';

USE northwind;

SELECT categoryid, categoryName , description 
FROM categories;

SELECT productid, productName
FROM products
WHERE discontinued = 1;

SELECT FirstName, ' ', lastname AS 'fullname'
FROM employees; 

SELECT CustomerID, CompanyName, Country
FROM customers
WHERE country IN ('Germany' , 'France');

SELECT COUNT(orderid)AS 'TotalOrders'
FROM orders;


SELECT supplierid, CompanyName, ContactName,ContactTitle
FROM suppliers 
WHERE contactTitle IN ('Sales representative' , 'Sales Manager');
-- where contactTitles == 'Sales Representative" or  "Sales manager"

SELECT customerID, contactName, orderid, companyName, OrderDate, shipAddress,address
FROM orders
JOIN customers USING (CustomerID)
ORDER BY orderdate;
-- LIMIT 5;

SELECT o.customerID, contactName, orderid, companyName, OrderDate, shipAddress,address,shipCity,city
FROM orders o
JOIN customers c ON o.shipCity = c.city
ORDER BY orderdate;
-- LIMIT 5;

-- Example 3
SELECT p. ProductName,
c. CategoryName,
p.UnitPrice
FROM products p
INNER JOIN categories c ON p.CategoryID = c.CategoryID
ORDER BY c. CategoryName, p.ProductName
LIMIT 6;
-- Example 5
-- custmores with zero oders will show 0 in order count 

SELECT c. companyName, 
COUNT(o.orderid) AS 'order count'
FROM customers c 
LEFT JOIN orders o ON c.CustomerID = o.CustomerID
GROUP BY C.companyName
ORDER BY 'order count' ASC
LIMIT 5;





USE northwind;
SELECT productid , productName , unitprice 
FROM products
ORDER BY unitprice ASC;
SELECT productid, productName , unitprice 
FROM products 
WHERE unitsinstock > 100
ORDER BY unitprice DESC;
SELECT productid, productName , unitprice 
FROM products 
WHERE unitsinstock < 100
ORDER BY unitprice DESC , productName ASC;
SELECT COUNT(DISTINCT customerid) AS customercount 
FROM orders;
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25
AND UnitsOnOrder > 0
ORDER BY UnitsOnOrder DESC, ProductName ASC;
SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title
ORDER BY EmployeeCount DESC;
SELECT FirstName, LastName, Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;



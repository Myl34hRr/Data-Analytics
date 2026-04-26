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
WHERE contactTitles IN ('Sales representative' , 'Sales Manger')





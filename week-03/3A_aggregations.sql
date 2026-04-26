USE northwind;
SELECT MIN(unitprice) AS cheapestprice 
FROM products;
-- finding the cheapest price item--

SELECT ProductName
FROM products
WHERE unitprice = (
SELECT MIN(UnitPrice)
FROM products);
-- finding the name of the cheapest item--
SELECT AVG(unitprice) AS averagerprice
FROM products;
-- finding the average price of all items that northwind sell--
-- rounding the number to the nearest cent will be 28.87--
SELECT MAX(unitprice) AS mostexpensive 
FROM products;
-- finding out the most expensive item northwind sells--
SELECT productName, unitprice
FROM products 
WHERE unitprice = (
SELECT MAX(unitprice)
FROM products);
-- finding the name of the expensive item sold--
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM northwind.employees;
-- finding the total monthly payroll--
SELECT MAX(salary) AS highestsalary, MIN(salary) AS lowestsalary
FROM products;
-- finding the highest and lowest salary that any employee makes--
SELECT s. supplierid, s. companyname,
COUNT(p. productid) AS numberofitems 
FROM suppliers s
JOIN products p
ON s.supplierid = p.supplierid 
GROUP BY s.supplierid, s.companyname;
-- finding the supplierid and the number of items they supply--
SELECT 
    c.CategoryName,
    AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;
-- list of all caategory names and the average price of the items--
SELECT 
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p
    ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;
-- suppliers that provide at least 5 items to northwind--
SELECT 
    ProductID,
    ProductName,
    UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY 
    InventoryValue DESC,
    ProductName ASC;
    -- list products currently in inventory by the product id, product name, and  inventory value--


USE northwind;
SELECT productid, productName , unitprice
FROM products 
JOIN suppliers 
ON products.supplierid = suppliers.supplierid
WHERE unitprice > 75
ORDER BY productName ASC;
SELECT products.productid, products.productName , products.unitprice, categories.categoryName, suppliers.companyName AS supplierName 
FROM products 
JOIN categories 
ON products.categoryid = categories.categoryid
JOIN suppliers 
ON products.supplierid = suppliers.supplierid
ORDER BY products.productName ASC;
SELECT 
    orders.OrderID,
    orders.ShipName,
    orders.ShipAddress,
    shippers.CompanyName AS Shipper
FROM orders
JOIN shippers
    ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'Germany'
ORDER BY Shipper ASC, orders.ShipName ASC;
SELECT 
    orders.ShipName,
    orders.ShipAddress,
    shippers.CompanyName AS Shipper,
    COUNT(*) AS OrderCount
FROM orders
JOIN shippers
    ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'Germany'
GROUP BY orders.ShipName, orders.ShipAddress, shippers.CompanyName
ORDER BY Shipper ASC, orders.ShipName ASC;
SELECT 
    orders.OrderID,
    orders.OrderDate,
    orders.ShipName,
    orders.ShipAddress
FROM orders
JOIN order_details 
    ON orders.OrderID = order_details.OrderID
JOIN products 
    ON order_details.ProductID = products.ProductID
WHERE products.ProductName = 'Sasquatch Ale';


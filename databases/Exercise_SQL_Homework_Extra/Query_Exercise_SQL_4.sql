SELECT *
    FROM Invoices
    ORDER BY Purchase_Date ASC;

SELECT *
    FROM Products
    ORDER BY Entry_Date DESC;

SELECT *
    FROM Products
    WHERE Price > 50000;

SELECT *
    FROM Products_Per_Invoice
    WHERE Products_Id = 10
    ORDER BY Total_Amount DESC;

SELECT *
    FROM Products_Per_Invoice
    WHERE Products_Id = 4;

SELECT Id, Products_Id, Total_Amount 
    FROM Products_Per_Invoice
    ORDER BY Products_Id DESC;

SELECT *
    FROM Invoices
    WHERE User_Id = 5;

SELECT * 
    FROM Invoices
    ORDER BY Total_Amount DESC;

SELECT * 
    FROM Invoices
    WHERE Id = 10;
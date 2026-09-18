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

-- Ya entendi mi error el problema era que el enunciado estaba pidiendo que
-- Agrupara "GROUP BY" no que ordenadara "OORDER BY" ahi fue mi confusion e
-- investigando me di cuenta que si quiero "GROUP BY" no debo incluir el "Id"
-- ya que el Id no se repite y "Product Id" si lo hace y "SUM" suma el total
-- de lo que cada "product Id" representa
SELECT 
    Products_Id, 
    SUM(Total_Amount) AS Total_Purchased
    FROM Products_Per_Invoice
    GROUP BY Products_Id
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
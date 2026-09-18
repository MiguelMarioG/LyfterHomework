INSERT INTO Products (Id, Name, Price, Stock_Available, Brand) VALUES
    (16, 'Servidor Dell PowerEdge', 78450.00, 5, 'Dell'),
    (17, 'Laptop HP ZBook Studio',  89200.50, 8, 'HP'),
    (18, 'Laptop Apple Gamer MSI Raider', 64500.00, 10, 'MSI'),
    (19, 'Camara RED Komodo 6K',     95800.00, 3, 'RED'),
    (20, 'Monitor Samsung Neo G9',  53999.90, 12, 'Samsung'),
    (21, 'Lente Canon RF 70-200mm',  58300.00, 7, 'Canon'),
    (22, 'Proyector 4K Laser',       72150.00, 4, 'Epson'),
    (23, 'Drone DJI Inspire 3 Kit',  98700.00, 2, 'DJI'),
    (24, 'Servidor NAS QNAP 16Bay',  61200.75, 6, 'QNAP'),
    (25, 'Consola Allen & Heath',   84900.00, 4, 'Allen & Heath');

SELECT *
    FROM Products;

SELECT *
    FROM Products
    WHERE Price > 50000
    ORDER BY Price DESC;

-- Como ya habia puesto los nuevos Values en la Tabla Products busque una manera
-- de buscar la palabra Apple dentro de uno de los nombres que estan en los Products
-- y me di cuenta que si le pongo este simbolo "%" lo puedo hacer y asi fue que hice
-- esta practica
SELECT *
    FROM Products
    WHERE Name LIKE '%Apple%';

SELECT *
    FROM Products
    ORDER BY Price DESC LIMIT 5;

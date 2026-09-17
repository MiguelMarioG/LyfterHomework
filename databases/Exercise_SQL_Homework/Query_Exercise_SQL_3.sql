INSERT INTO Products (Id, Name, Price, Entry_Date, Brand, Stock_Available) VALUES
    (1, 'Laptop ThinkPad X1', 51299.99, '2024-01-15', 'Lenovo', 15),
    (2, 'iPhone 15 Pro', 3999.00, '2024-01-20', 'Apple', 25),
    (3, 'Galaxy S24 Ultra', 2199.50, '2024-02-01', 'Samsung', 18),
    (4, 'Monitor UltraSharp 27"', 1349.99, '2024-02-10', 'Dell', 40),
    (5, 'Teclado Mecánico MX Keys', 1109.90, '2024-02-12', 'Logitech', 60),
    (6, 'Smart TV OLED 55"', 61399.00, '2024-02-18', 'LG', 10),
    (7, 'Audífonos WH-1000XM5', 1380.00, '2024-02-25', 'Sony', 30),
    (8, 'Console PlayStation 5', 1499.99, '2024-03-01', 'Sony', 12),
    (9, 'Tablet iPad Air', 2599.00, '2024-03-05', 'Apple', 22),
    (10, 'Mouse MX Master 3S', 199.99, '2024-03-10', 'Logitech', 45),
    (11, 'Smartwatch Galaxy Watch 6', 1249.50, '2024-03-12', 'Samsung', 28),
    (12, 'Altavoz Bluetooth Flip 6', 1129.95, '2024-03-15', 'JBL', 50),
    (13, 'SSD Externo T7 1TB', 389.99, '2024-03-18', 'Samsung', 75),
    (14, 'Impresora LaserJet Pro', 1219.00, '2024-03-20', 'HP', 14),
    (15, 'Camara EOS R6', 52299.00, '2024-03-22', 'Canon', 8);

INSERT INTO Users ( Id, Full_Name, Buyer_Email, Registration_Date) VALUES
    (1, 'Carlos Mendoza', 'carlos.mendoza@email.com', '2024-01-10'),
    (2, 'Ana Sofía Rodríguez', 'ana.rodriguez@email.com', '2024-01-14'),
    (3, 'Mateo Gómez', 'mateo.gomez@email.com', '2024-01-22'),
    (4, 'Valeria Fernández', 'valeria.f@email.com', '2024-02-01'),
    (5, 'Lucas Silva', 'lucas.silva@email.com', '2024-02-05'),
    (6, 'Camila Torrez', 'camila.torrez@email.com', '2024-02-12'),
    (7, 'Diego Morales', 'diego.morales@email.com', '2024-02-18'),
    (8, 'Mariana López', 'mariana.lopez@email.com', '2024-02-25'),
    (9, 'Javier Herrera', 'javier.herrera@email.com', '2024-03-02'),
    (10, 'Isabella Benítez', 'isabella.b@email.com', '2024-03-08'),
    (11, 'Gabriel Castro', 'gabriel.castro@email.com', '2024-03-11'),
    (12, 'Daniela Navarro', 'daniela.navarro@email.com', '2024-03-15'),
    (13, 'Alejandro Vargas', 'alejandro.v@email.com', '2024-03-19'),
    (14, 'Sofia Romero', 'sofia.romero@email.com', '2024-03-22'),
    (15, 'Tomás Gutiérrez', 'tomas.gutierrez@email.com', '2024-03-27');

INSERT INTO Payment_Methods ( Id, Method_Type, Bank_Name) VALUES
    (1, 'Paypal', NULL),
    (2, 'Zelle', 'Chase'),
    (3, 'Venmo', NULL),
    (4, 'Transferencia', 'Bank of America'),
    (5, 'Tarjeta de Débito', 'Wells Fargo'),
    (6, 'Paypal', NULL),
    (7, 'Zelle', 'Citibank'),
    (8, 'Venmo', NULL),
    (9, 'Tarjeta de Crédito', 'Capital One'),
    (10, 'Zelle', 'PNC Bank'),
    (11, 'Paypal', NULL),
    (12, 'Transferencia', 'TD Bank'),
    (13, 'Venmo', NULL),
    (14, 'Zelle', 'U.S. Bank'),
    (15, 'Paypal', NULL);

INSERT INTO Invoices (Id, User_Id, Purchase_Date, Total_Amount, Phone_Number,Employee_Code) VALUES
    (1, 1, '2024-02-01', 52409.89, 14155550101, 104), -- (1 Laptop ThinkPad X1: 51299.99 + 1 Teclado MX Keys: 1109.90)
    (2, 1, '2024-02-15', 399.98,   14155550101, 104), -- (2 Mouses MX Master 3S: 199.99 * 2)
    (3, 2, '2024-02-10', 5379.00,  12125550122, 208), -- (1 iPhone 15 Pro: 3999.00 + 1 Audífonos WH-1000XM5: 1380.00)
    (4, 3, '2024-02-18', 2199.50,  13055550143, 104), -- (1 Galaxy S24 Ultra: 2199.50)
    (5, 4, '2024-02-20', 2479.94,  17135550164, 305), -- (1 Monitor UltraSharp: 1349.99 + 1 Altavoz Flip 6: 1129.95)
    (6, 5, '2024-02-22', 62898.99, 13125550185, 208), -- (1 Smart TV OLED: 61399.00 + 1 PS5: 1499.99)
    (7, 5, '2024-03-01', 779.98,   13125550185, 104), -- (2 SSD Externos T7 1TB: 389.99 * 2)
    (8, 6, '2024-03-02', 3979.00,  12065550196, 305), -- (1 Audífonos WH-1000XM5: 1380.00 + 1 Tablet iPad Air: 2599.00)
    (9, 7, '2024-03-05', 2849.49,  16175550117, 401), -- (1 PS5: 1499.99 + 1 Monitor UltraSharp: 1349.99)
    (10, 8, '2024-03-08', 2599.00,  12145550138, 208), -- (1 Tablet iPad Air: 2599.00)
    (11, 9, '2024-03-10', 1309.89,  14085550159, 104), -- (1 Mouse MX Master 3S: 199.99 + 1 Teclado MX Keys: 1109.90)
    (12, 10, '2024-03-12', 3449.00, 16025550170, 305), -- (1 Smartwatch Galaxy Watch 6: 1249.50 + 1 Galaxy S24 Ultra: 2199.50)
    (13, 11, '2024-03-15', 2259.90, 14045550181, 401), -- (2 Altavoces Flip 6: 1129.95 * 2)
    (14, 12, '2024-03-18', 1608.99, 17025550192, 104), -- (1 Impresora LaserJet: 1219.00 + 1 SSD T7 1TB: 389.99)
    (15, 15, '2024-03-28', 56298.00, 16195550115, 208);-- (1 Cámara EOS R6: 52299.00 + 1 iPhone 15 Pro: 3999.00)

INSERT INTO Reviews (Id, Products_Id, Users_Id, Comment, Rating, Date) VALUES
    (1, 1, 1, 'Excelente laptop para trabajar. El rendimiento es increíble y la pantalla tiene muy buen brillo.', 5, '2024-02-02'),
    (2, 5, 1, 'El teclado mecánico se siente de muy buena calidad. Teclas muy cómodas para escribir horas.', 4, '2024-02-16'),
    (3, 2, 2, 'El iPhone 15 Pro es muy rápido y la cámara es brutal, aunque la batería podría durar un poco más.', 4, '2024-02-11'),
    (4, 7, 2, 'La cancelación de ruido de estos audífonos Sony es impresionante. Cómodos para viajes largos.', 5, '2024-02-12'),
    (5, 3, 3, 'El Galaxy S24 Ultra tiene una pantalla espectacular y el lápiz stylus funciona muy fluido.', 5, '2024-02-19'),
    (6, 4, 4, 'El monitor Dell tiene una resolución genial para diseño gráfico. Los colores vienen bien calibrados.', 4, '2024-02-21'),
    (7, 12, 4, 'Buen altavoz Bluetooth, el sonido es potente para su tamaño pero le faltan algo de graves.', 3, '2024-02-22'),
    (8, 6, 5, 'La pantalla OLED de esta TV es de otro mundo. Los negros son totalmente puros, ideal para películas.', 5, '2024-02-23'),
    (9, 8, 5, 'La consola es rápida y silenciosa, pero los juegos digitales ocupan demasiado espacio.', 4, '2024-02-24'),
    (10, 13, 5, 'El SSD Samsung T7 vuela transfiriendo archivos grandes. Súper compacto y resistente.', 5, '2024-03-02'),
    (11, 7, 6, 'Llegaron a to pero elaque vino un poco aplastado. Los audífonos funcionan bien.', 1, '2024-03-03'),
    (12, 9, 6, 'La Tablet iPad Air es muy liviana y la pantalla se ve increíble. Perfecta para tomar notas.', 5, '2024-03-04'),
    (13, 10, 9, 'El mouse MX Master 3S es ultra ergonómico y el desplazamiento rápido ayuda muchísimo en la oficina.', 5, '2024-03-11'),
    (14, 11, 10, 'Buen reloj inteligente para monitorear el ejercicio diario, aunque hay que cargarlo todos los días.', 3, '2024-03-13'),
    (15, 15, 15, 'Cámara profesional de altísimo nivel. La calidad de imagen en condiciones de poca luz es fantástica.', 5, '2024-03-29');

INSERT INTO Shopping_Cart (Id, User_Id) VALUES
    (1, 5),
    (2, 2),
    (3, 12),
    (4, 1),
    (5, 8),
    (6, 15),
    (7, 3),
    (8, 14),
    (9, 7),
    (10, 10),
    (11, 4),
    (12, 11),
    (13, 6),
    (14, 9),
    (15, 13);

INSERT INTO Cart_Items (Id, Shopping_Cart_Id, Products_Id, Quantity) VALUES
    (1, 1, 6, 1),   -- Smart TV OLED 55"
    (2, 1, 8, 1),   -- PlayStation 5
    (3, 1, 7, 2),   -- Audífonos WH-1000XM5
    (4, 2, 2, 1),   -- iPhone 15 Pro
    (5, 2, 9, 1),   -- Tablet iPad Air
    (6, 3, 14, 1),  -- Impresora LaserJet Pro
    (7, 3, 4, 2),   -- Monitor UltraSharp 27"
    (8, 3, 5, 1),   -- Teclado Mecánico MX Keys
    (9, 3, 10, 1),  -- Mouse MX Master 3S
    (10, 4, 1, 1),  -- Laptop ThinkPad X1
    (11, 4, 5, 1),  -- Teclado Mecánico MX Keys
    (12, 4, 13, 2), -- SSD Externo T7 1TB
    (13, 5, 3, 1),  -- Galaxy S24 Ultra
    (14, 5, 11, 1), -- Smartwatch Galaxy Watch 6
    (15, 6, 15, 1), -- Cámara EOS R6
    (16, 6, 13, 1), -- SSD Externo T7 1TB
    (17, 6, 7, 1),  -- Audífonos WH-1000XM5
    (18, 7, 3, 1),  -- Galaxy S24 Ultra
    (19, 7, 12, 2), -- Altavoz Bluetooth Flip 6
    (20, 8, 4, 1),  -- Monitor UltraSharp 27"
    (21, 8, 5, 1),  -- Teclado Mecánico MX Keys
    (22, 8, 10, 1), -- Mouse MX Master 3S
    (23, 8, 12, 1), -- Altavoz Bluetooth Flip 6
    (24, 9, 8, 1),  -- PlayStation 5
    (25, 9, 12, 3), -- Altavoz Bluetooth Flip 6
    (26, 10, 11, 1), -- Smartwatch Galaxy Watch 6
    (27, 10, 3, 1),  -- Galaxy S24 Ultra
    (28, 10, 10, 1), -- Mouse MX Master 3S
    (29, 11, 1, 1),  -- Laptop ThinkPad X1
    (30, 11, 4, 2),  -- Monitor UltraSharp 27"
    (31, 11, 5, 1),  -- Teclado Mecánico MX Keys
    (32, 11, 10, 1), -- Mouse MX Master 3S
    (33, 11, 13, 2), -- SSD Externo T7 1TB
    (34, 12, 12, 2), -- Altavoz Bluetooth Flip 6
    (35, 12, 7, 1),  -- Audífonos WH-1000XM5
    (36, 13, 9, 1),  -- Tablet iPad Air
    (37, 13, 2, 1),  -- iPhone 15 Pro
    (38, 13, 7, 1),  -- Audífonos WH-1000XM5
    (39, 14, 10, 2), -- Mouse MX Master 3S
    (40, 14, 5, 1),  -- Teclado Mecánico MX Keys
    (41, 15, 13, 3), -- SSD Externo T7 1TB
    (42, 15, 14, 1), -- Impresora LaserJet Pro
    (43, 15, 4, 1);  -- Monitor UltraSharp 27"

INSERT INTO Invoice_Payment (Id, Invoice_Id, Payment_Method_Id, Amount_Paid) VALUES
    (1, 1, 1, 52409.89),
    (2, 2, 3, 399.98),
    (3, 3, 2, 5379.00),
    (4, 4, 4, 2199.50),
    (5, 5, 5, 2479.94),
    (6, 6, 6, 62898.99),
    (7, 7, 7, 779.98),
    (8, 8, 8, 3979.00), 
    (9, 9, 9, 2849.49), 
    (10, 10, 10, 2599.00),
    (11, 11, 11, 1309.89),
    (12, 12, 12, 3449.00),
    (13, 13, 13, 2259.90),
    (14, 14, 14, 1608.99),
    (15, 15, 15, 56298.00);

INSERT INTO Products_Per_Invoice ( Id, Invoice_Id, Products_Id, Quantity, Total_Amount) VALUES
    (1, 1, 1, 2, 102599.98),  -- 2 * 51299.99
    (2, 1, 5, 3, 3329.70),    -- 3 * 1109.90
    (3, 2, 10, 3, 599.97),    -- 3 * 199.99
    (4, 3, 2, 1, 3999.00),    -- 1 * 3999.00
    (5, 3, 7, 2, 2760.00),    -- 2 * 1380.00
    (6, 4, 3, 2, 4399.00),    -- 2 * 2199.50
    (7, 5, 4, 2, 2699.98),    -- 2 * 1349.99
    (8, 5, 12, 2, 2259.90),   -- 2 * 1129.95
    (9, 6, 6, 1, 61399.00),   -- 1 * 61399.00
    (10, 6, 8, 2, 2999.98),   -- 2 * 1499.99
    (11, 7, 13, 4, 1559.96),  -- 4 * 389.99
    (12, 8, 7, 2, 2760.00),   -- 2 * 1380.00
    (13, 8, 9, 1, 2599.00),   -- 1 * 2599.00
    (14, 9, 8, 2, 2999.98),   -- 2 * 1499.99
    (15, 9, 4, 1, 1349.99),   -- 1 * 1349.99
    (16, 10, 9, 2, 5198.00),  -- 2 * 2599.00
    (17, 11, 10, 2, 399.98),  -- 2 * 199.99
    (18, 11, 5, 2, 2219.80),  -- 2 * 1109.90
    (19, 12, 11, 2, 2499.00), -- 2 * 1249.50
    (20, 12, 3, 1, 2199.50),  -- 1 * 2199.50
    (21, 13, 12, 3, 3389.85), -- 3 * 1129.95
    (22, 14, 14, 2, 2438.00), -- 2 * 1219.00
    (23, 14, 13, 3, 1169.97), -- 3 * 389.99
    (24, 15, 15, 1, 52299.00),-- 1 * 52299.00
    (25, 15, 2, 2, 7998.00);  -- 2 * 3999.00

-- Como quice hacer mas interesante la Tabla de Products_Per_Invoice se me habia olvidad que podia
-- tener una columna de Quiantity asi que agrege varios productos comprados en un mismo Invoice
-- pero como ya habia hecho las cantidades en las Tablas de Invoices y de Invoice_Payment entonces
-- Actualice la columna Total_Amount en la tabla Invoices y tambien la columna Amount_Paid en la
-- Tabla Invoice_Payment para que codo coincida.

UPDATE Invoices SET Total_Amount = 105929.68  WHERE Id = 1;
UPDATE Invoices SET Total_Amount = 599.97     WHERE Id = 2;
UPDATE Invoices SET Total_Amount = 6759.00    WHERE Id = 3;
UPDATE Invoices SET Total_Amount = 4399.00    WHERE Id = 4;
UPDATE Invoices SET Total_Amount = 4959.88    WHERE Id = 5;
UPDATE Invoices SET Total_Amount = 64398.98   WHERE Id = 6;
UPDATE Invoices SET Total_Amount = 1559.96    WHERE Id = 7;
UPDATE Invoices SET Total_Amount = 5359.00    WHERE Id = 8;
UPDATE Invoices SET Total_Amount = 4349.97    WHERE Id = 9;
UPDATE Invoices SET Total_Amount = 5198.00    WHERE Id = 10;
UPDATE Invoices SET Total_Amount = 2619.78    WHERE Id = 11;
UPDATE Invoices SET Total_Amount = 4698.50    WHERE Id = 12;
UPDATE Invoices SET Total_Amount = 3389.85    WHERE Id = 13;
UPDATE Invoices SET Total_Amount = 3607.97    WHERE Id = 14;
UPDATE Invoices SET Total_Amount = 60297.00   WHERE Id = 15;

UPDATE Invoice_payment SET Amount_Paid = 105929.68  WHERE Invoice_Id = 1;
UPDATE Invoice_payment SET Amount_Paid = 599.97     WHERE Invoice_Id = 2;
UPDATE Invoice_payment SET Amount_Paid = 6759.00    WHERE Invoice_Id = 3;
UPDATE Invoice_payment SET Amount_Paid = 4399.00    WHERE Invoice_Id = 4;
UPDATE Invoice_payment SET Amount_Paid = 4959.88    WHERE Invoice_Id = 5;
UPDATE Invoice_payment SET Amount_Paid = 64398.98   WHERE Invoice_Id = 6;
UPDATE Invoice_payment SET Amount_Paid = 1559.96    WHERE Invoice_Id = 7;
UPDATE Invoice_payment SET Amount_Paid = 5359.00    WHERE Invoice_Id = 8;
UPDATE Invoice_payment SET Amount_Paid = 4349.97    WHERE Invoice_Id = 9;
UPDATE Invoice_payment SET Amount_Paid = 5198.00    WHERE Invoice_Id = 10;
UPDATE Invoice_payment SET Amount_Paid = 2619.78    WHERE Invoice_Id = 11;
UPDATE Invoice_payment SET Amount_Paid = 4698.50    WHERE Invoice_Id = 12;
UPDATE Invoice_payment SET Amount_Paid = 3389.85    WHERE Invoice_Id = 13;
UPDATE Invoice_payment SET Amount_Paid = 3607.97    WHERE Invoice_Id = 14;
UPDATE Invoice_payment SET Amount_Paid = 60297.00   WHERE Invoice_Id = 15;
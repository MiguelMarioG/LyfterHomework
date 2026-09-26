INSERT INTO Items (ID, Item_name, Price) VALUES
(101, 'CheeseBurger', '$8'),
(102, 'Fries', '$3'),
(103, 'Pizza', '$12'),
(104, 'Soda', '$2'),
(105, 'Salad', '$6'),
(106, 'Water', '$1');

INSERT INTO Customers (ID, Customer_Name, Customer_Phone, Address) VALUES
    (1, 'Alice Mendoza', '123-456-7890', '123 Main St'),
    (2, 'Bob García', '987-654-3210', '465 Elm St'),
    (3, 'Claire Rodríguez', '555-123-4567', '789 Oak St'),
    (4, 'Ana Martínez', '555-456-7890', '101 Sunset Blvd'),
    (5, 'Luis Hernández', '555-567-8901', '220 Ocean Dr'),
    (6, 'Sofia López', '555-678-9012', '500 Pine St'),
    (7, 'Diego Pérez', '555-789-0123', '304 Congress Ave'),
    (8, 'Elena Gomez', '555-890-1234', '808 Broadway'),
    (9, 'Fernando Sánchez', '555-901-2345', '150 Peachtree St'),
    (10, 'Patricia Torres', '555-012-3456', '600 Las Vegas Blvd');

INSERT INTO Orders (ID, Customers_Id, Delivery_Time) VALUES
    (001, 1, '6:00PM'),
    (002, 2, '7:30PM'),
    (003, 3, '12:00PM'),
    (004, 3, '5:00PM');

INSERT INTO Order_Items (ID, Orders_Id, Items_Id, Quantity, Special_Request) VALUES
(1, 001, 101, 2, 'No Onion'),
(2, 001, 102, 1, 'Extra Ketchup'),
(3, 002, 103, 1, 'Extra Cheese'),
(4, 002, 102, 2, 'None'),
(5, 003, 105, 1, 'No Croutons'),
(6, 004, 106, 1, 'None');
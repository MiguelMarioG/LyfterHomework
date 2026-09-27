INSERT INTO Authors (ID, Author_Name) VALUES
    (001, 'Miguel de Cervantes'),
    (002, 'Dante Alighieri'),
    (003, 'Takehiko Inoue'),
    (004, 'Akira Toriyama'),
    (005, 'Walt Disney');

INSERT INTO Books (ID, Book_Name, Authors_Id) VALUES
    (001, 'Don Quijote', 001),
    (002, 'La Divina Comedia', 002),
    (003, 'Vagabond 1-3', 003),
    (004, 'Dragon Ball 1', 004),
    (005, 'The Book of the 5 Rings', NULL);

INSERT INTO Customers (ID, Customer_Name, Customer_Email) VALUES
    (001, 'John Doe', 'j.doe@email.com'),
    (002, 'Jane Doe', 'jane@doe.com'),
    (003, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO Rents (ID, Books_Id, Customers_Id, State) VALUES
    (001, 001, 002, 'Returned'),
    (002, 002, 002, 'Returned'),
    (003, 001, 001, 'On time'),
    (004, 003, 001, 'On time'),
    (005, 002, 002, 'Overdue');
-- Aqui fue un INNER JOIN normal para moestrar todo lo que tiene relacion entre
-- las dos tablas escluyendo la unica que tiene NULL en su Authors_Id
SELECT Books.Book_Name, Authors.Author_Name
FROM Books AS books
INNER JOIN Authors AS authors
ON books.Authors_Id = authors.ID;

-- Aqui tuvimos que usar un WhERE para especificar que Authors_Id IS NULL
SELECT Books.Book_Name, Authors.Author_Name
FROM Books AS books
LEFT JOIN Authors AS authors
    ON books.Authors_Id = authors.ID
WHERE books.Authors_Id IS NULL;

-- Para este Query intente hacer el RIGHT JOIN pero SQLite me mando un error de que
-- RIGHT y FULL OUTER JOINs no los soporta actualmente la version de SQLite
SELECT Books.Book_Name, Authors.Author_Name
FROM Authors as authors
LEFT JOIN Books AS books
    ON books.Authors_Id = authors.ID
WHERE books.Authors_Id IS NULL;

-- en este Query investigue que podia usa rl DISTINCT para eliminar si un libro podia
-- aparecer varias veces en la tabla de Rents y de esa manera mostrar los libros que en
-- algun momento han sido rentados y como sus ID aparecen en la tabla Rents significa
-- que en algun momento fueron rentados
SELECT DISTINCT Books.Book_Name
FROM Books AS books
INNER JOIN Rents AS rents
    ON books.ID = rents.Books_Id;

-- este Query lo hice nada mas para probar el GROUP BY
SELECT DISTINCT Books.Book_Name, Rents.State
FROM Books AS books
INNER JOIN Rents AS rents
    ON books.ID = rents.Books_Id
GROUP BY Books.ID;

-- Aqui no se puede usar un INNER JOIN porque el INNER JOIN no muestra nunca los valores
-- NULL en las tablas asi que debemos usar el LEFT JOIN porque aparte el RIGHT JOIN no
-- esta siendo soportado por SQLite
SELECT Books.Book_Name
FROM Books AS books
LEFT JOIN Rents AS rents
    ON books.ID = rents.Books_Id
WHERE rents.Books_Id IS NULL;

-- Extra Query
SELECT Books.Book_Name, Rents.State
FROM Books AS books
LEFT JOIN Rents AS rents
    ON books.ID = rents.Books_Id
WHERE rents.Books_Id IS NULL;

-- Este Query da el customer que no a rentado nada
SELECT Customers.Customer_Name
FROM Customers AS customers
LEFT JOIN Rents AS rents
    ON customers.ID = rents.Customers_Id
WHERE rents.Customers_Id IS NULL;

-- ultimo Queey que muestra solo los que tiene estatus de Overdue
SELECT Books.Book_Name, Rents.State
FROM Books AS books
LEFT JOIN Rents AS rents
    ON books.ID = rents.Books_Id
WHERE rents.State = 'Overdue';
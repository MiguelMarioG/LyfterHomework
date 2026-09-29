-- Aqui usamos el COUNT para crear una tabla que nos va a mostrar el numero
-- de veces que un customer a rentado un libro y esa tabla solo va a vivir
-- momentaneamente en la RAM en lo que mostramos los datos con el QUERY y
-- dandonos el resultado
SELECT 
    customers.Customer_Name,
    COUNT(rents.Customers_Id) AS total_rents
FROM Rents AS rents
INNER JOIN Customers AS customers
    ON rents.Customers_Id = customers.ID
GROUP BY rents.Customers_Id
ORDER BY total_rents DESC
LIMIT 3;


-- Aqui usamos varios JOIN por la simple razon que me pidieron varios valores
-- que residen en la tabla de Rents haciendo que saquemos los INNER JOIN de los
-- valores en los que no tenemos nada NULL y un LEFT JOIN para sacar el valor
-- donde reside un valor NULL y no debemos hacer nada en State ya que es un valor
-- que reside en Rents por si misma sin necesidad de compararla con otra tabla
SELECT
    customers.Customer_Name,
    books.Book_Name,
    authors.Author_Name,
    rents.State
FROM Rents AS rents
INNER JOIN Customers AS customers 
    ON rents.Customers_Id = customers.ID
INNER JOIN Books AS books 
    ON rents.Books_Id = books.ID
LEFT JOIN Authors AS authors 
    ON books.Authors_Id = authors.ID;
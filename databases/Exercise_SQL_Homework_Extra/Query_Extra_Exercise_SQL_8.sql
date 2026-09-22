-- Primero corri esta linea para establecer el precio de varios productos en "0"
-- Ya que reuse la Base de datos que hice en el ejercicio 1 con cantidades y todo
-- establecido para hacerlo como lo pide el ejercicio extra inicialice algunas a "0"
UPDATE Products SET Price = 0 WHERE Id IN (11, 17, 4);
UPDATE Products SET Price = -234 WHERE Id IN (20, 23, 18);

-- -- Ahora Corri esta linea para establecer el stock_available en "0"
UPDATE Products SET Stock_Available = 0 WHERE Price <= 0;

-- -- Investigue y al parecer SQLite no es como Python no podemos usar "+="
-- -- se tiene que hacer variable = variable + cantidad
UPDATE Products SET Price = Price + 100 WHERE Stock_Available < 10;

-- -- Ahora se que el ejercicio dice que aumente el "Price" 100 unidades cuando
-- -- "Stock_Available" es menor que "10" pero me imagino que la variable que 
-- -- tenemos que cambiar es "Stock_Available", en lugar que "Price" para
-- -- Aumentar el Stock ya que no tenemos tanto Stock en la Bodega por eso
-- -- Propongo esta siguiente linea de Codigo
UPDATE Products SET Stock_Available = Stock_Available + 100 WHERE Stock_Available < 10;

UPDATE Products SET Stock_Available = 1 WHERE Id IN (6, 3, 25);

SELECT *
    FROM Products
    ORDER BY Id ASC 
    LIMIT 10;
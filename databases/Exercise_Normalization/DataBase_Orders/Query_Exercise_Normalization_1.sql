-- lA Normalizacion empezo basandome en que es lo que tenia que dividir y hacerlo segun la
-- divisiones de la data repetida y que podia o debia ser dividida en su resptectiva tabla
-- de esta manera tenemos la primera tabla que es la de Items que guarda el nombre de lo que
-- se vende en el restaurant con su respectivo precio.
CREATE TABLE Items (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Item_name VARCHAR (25) NOT NULL UNIQUE,
    Price VARCHAR (15) NOT NULL DEFAULT 0
);

-- Ahora seguimos con la tabla de Customers que segun su registro tenemos sus "Id", su nombre,
-- su telefono y por ultimo su direccion entonces para que esos datos no se esten repitiendo
-- constantemente en una sola tabla la podemos dividir como las anteriores para normalizar y
-- organizar mejor todos los datos.
CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_Name VARCHAR (30) NOT NULL UNIQUE,
    Customer_Phone VARCHAR (20) NOT NULL,
    Address VARCHAR (100) NOT NULL
);

-- Ahora tenemos la tabla de Orders que debe registrar las Ordenes segun si la hora en la que
-- la efectua el customer ya que debemos registrar si un customer hace varias ordenes a una misma
-- hora y juntarlas.
CREATE TABLE Orders (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customers_Id INTEGER REFERENCES Customers (ID),
    Delivery_Time VARCHAR (10)
);

-- Por ultimo tenemos la tabla de Order_Items que debe tener la informacion de todo lo demas para
-- organizar todo y normalizar todo perfecto tomando los ID para no repetir informacion.
CREATE TABLE Order_Items (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Orders_Id INTEGER REFERENCES Orders (ID),
    Items_Id INTEGER REFERENCES Items (ID),
    Quantity SMALLINT NOT NULL DEFAULT 0,
    Special_Request TEXT NULL
);
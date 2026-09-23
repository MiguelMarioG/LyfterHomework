CREATE TABLE Policy (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Policy_Type VARCHAR (30)
);

-- Aqui estoy creando 4 tablas en esta que es la primera ense en dividir uno de los
-- fields que podrian repetirse porque un carro podria tener una Insurance Policy en una
-- misma compañia e incluimos la columna "Isurance_Policy" porque va ligado a la Insurance
CREATE TABLE Insurance (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Insurance_Company VARCHAR (25) NOT NULL
);

-- Aqui estamos creando la tabla que corresponde a los Owners de los carros haciendo que
-- organicemos a los dueños de los diferentes carros por orden con sus "ID"
CREATE TABLE Owners (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Owner_Name VARCHAR (30) NOT NULL,
    Owner_Phone VARCHAR (10) NOT NULL UNIQUE
);

-- Me di cuenta que "Make" se repite varias veces y estamos seguros que siempre vamos a
-- hacer referencia a que si tenemos un civic o un accord si o si representa un Honda asi
-- que para mejor organizacion decidi hacer una tabla para Make de los distintos carros asi
-- podemos tener mejor organizacion.
CREATE TABLE Makes (
    ID INTEGER PRIMARY KEY,
    Make VARCHAR (20) NOT NULL
);

CREATE TABLE Models (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Makes_Id INTEGER REFERENCES Makes (ID),
    Model_Name VARCHAR (25),
    Year INTEGER NOT NULL
);

-- Para tener datos de los carros creamos su tabla que el VIN nos va a servir para que
-- formen como primary key y esto nos da la mejor manera de tener los carros para darle
-- la referencia de quien tiene como dueño que tipo de carro
CREATE TABLE Cars (
    VIN VARCHAR (20) PRIMARY KEY,
    Models_Id INTEGER REFERENCES Models (ID),
    Color_Type VARCHAR (25) NOT NULL
);

-- Esta es la ultima tabla que nos relaciona todo ya que aqui tenemos casi todas las FK
-- que nos hace esta la tabla cruz que relaciona todo para saber que carro tiene que owner
-- y que insurance
CREATE TABLE Cars_Ownership (
    ID INTEGER PRIMARY KEY,
    Cars_VIN VARCHAR (20) REFERENCES Cars (VIN),
    Owners_Id INTEGER REFERENCES Owners (ID),
    Insurance_Id INTEGER REFERENCES Insurance (ID),
    Policy_Id INTEGER REFERENCES Policy (ID)
);
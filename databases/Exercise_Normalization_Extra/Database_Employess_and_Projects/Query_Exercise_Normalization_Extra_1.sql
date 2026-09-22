-- Para empezar la Normalizacion de este proyecto tuve que ver la tabla ejemplo
-- que nos dieron y me di cuenta como es que el Id de employee se repite varias
-- veces como tambien el nombre y el departamento.

-- Ahora como employee es solo un nombre que llevaria su tabla nos conviene
-- hacer la tabla de employee para  evitar la repeticion y ademas seguimos 
-- con las siguientes columnas que son las de department decidi crear la tabla
-- de department ya que deparment phone depende de department ya que es 
-- un telefono vinculado al department en el que el employee esta vinculado

-- y por ultimo tenemos los porject que todo va a estar relacionado con la tabla
-- hecha de porject ya que al momento es uno de los values que no se repiten
-- asi que dependiendo del proyecto se van a relacionar los employees que esten
-- relacionado con el departamento en el que esten

-- Asi fue como llegue a la normalizacion de la tabla que me dieron y resumirla
-- a estas 3 tablas para normalizar este ejercicio. Ademas me fije en unos ejemplos
-- que podia referencia las FK de la forma en la que lo hice en este ejercicio.

CREATE TABLE Employee (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_Name VARCHAR (30) UNIQUE
);

CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Department VARCHAR (25) UNIQUE,
    Department_Phone VARCHAR (15) UNIQUE
);

CREATE TABLE Projects (
    ID VARCHAR (25) PRIMARY KEY,
    Project_Name VARCHAR (30),
    Project_Budget FLOAT NOT NULL DEFAULT 0,
    Employee_Id INTEGER NOT NULL,
    Departments_Id INTEGER NOT NULL,
    FOREIGN KEY (Employee_Id) REFERENCES Employee (ID),
    FOREIGN KEY (Departments_Id) REFERENCES Departments (ID)
);
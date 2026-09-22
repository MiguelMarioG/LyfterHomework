-- Para hacer la normalizacion de la siguiente tabla se tuvo que ver que muchos
-- datos se encontraban repetidos y con la opcion de organizar cada uno en sus
-- respectivas tablas, por eso pense en hacer primero las 3 primeras tablas
-- que manejaban las dependencias mas claras ya que para tener mas organizado
-- los estudiantes tendrian su ID y nombre, los cursos sus ID y nombres y 
-- por ulitmo serian los instructores con su ID y su unique email, pero para hacer
-- que todo se relacion tuvimos que hacer la tabla Class_Register que sirve como
-- tabla cruz que relaciona todos los datos de todas las tablas para que puedan
-- normalizarce y quedar organizadas.

CREATE TABLE Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_Name VARCHAR (30) NOT NULL
);

CREATE TABLE Courses (
    ID VARCHAR (25) PRIMARY KEY,
    Course_Name VARCHAR (30) NOT NULL
);

CREATE TABLE Intructors (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Instructor_Name VARCHAR (30) NOT NULL,
    Instructor_Email VARCHAR (30) NOT NULL UNIQUE
);

CREATE TABLE Class_Register (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Students_Id INTEGER NOT NULL,
    Courses_Id VARCHAR (25) NOT NULL,
    Instructors_Id INTEGER NOT NULL,
    FOREIGN KEY (Students_Id) REFERENCES Students (ID),
    FOREIGN KEY (Courses_Id) REFERENCES Courses (ID),
    FOREIGN KEY (Instructors_Id) REFERENCES Instructors (ID)
);
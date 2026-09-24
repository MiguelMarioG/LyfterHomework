-- me equivoque al nombrar la tabla asi que aproveche este error para practicar
-- el ALTER y modificar el nombre de la tabla que esta mal escrita en mi Query anterior
ALTER TABLE Intructors RENAME TO Instructors;

INSERT INTO Students (ID, Student_Name) VALUES
    (301, 'Marco Gómez'),
    (302, 'Carla Ruiz');

INSERT INTO Instructors (ID, Instructor_Name, Instructor_Email) VALUES
    (101, 'Juan Pérez', 'juan@uni.edu'),
    (102, 'Laura Rojas', 'laura@uni.edu');

INSERT INTO Courses (ID, Course_Name, Instructors_Id) VALUES
    ('CS101', 'Python I', 101),
    ('CS102', 'Python II', 102);

INSERT INTO Class_Register (ID, Students_Id, Courses_Id) VALUES
    (201, 301, 'CS101'),
    (202, 301, 'CS102'),
    (203, 302, 'CS101');

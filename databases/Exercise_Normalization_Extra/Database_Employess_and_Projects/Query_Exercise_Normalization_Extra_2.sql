INSERT INTO Departments (ID, Department, Department_Phone) VALUES
    (001, 'IT', '2222-2222'),
    (002, 'Marketing', '1111-1111');

INSERT INTO Employee (ID, Employee_Name, Departments_Id) VALUES
    (201, 'Ana Rivera', 001),
    (202, 'Luis Mendez', 002);

INSERT INTO Projects (ID, Project_Name, Project_Budget) VALUES
    ('P001', 'Web App', 50000.50),
    ('P002', 'API REST', 25000.95),
    ('P003', 'TV Campaign', 30000.45);

INSERT INTO Project_Allocation (Projects_Id, Employee_Id, Assigned_Date) VALUES
    ('P001', 201, '2018-05-20'),
    ('P002', 201, '2020-08-15'),
    ('P003', 202, '2010-04-30'),
    ('P001', 202, '2023-10-10');
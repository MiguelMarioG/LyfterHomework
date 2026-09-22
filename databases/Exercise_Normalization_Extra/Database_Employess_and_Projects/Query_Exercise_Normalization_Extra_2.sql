INSERT INTO Employee (ID, Employee_Name) VALUES
    (201, 'Ana Rivera'),
    (202, 'Luis Mendez');

INSERT INTO Departments (ID, Department, Department_Phone) VALUES
    (001, 'IT', '2222-2222'),
    (002, 'Marketing', '1111-1111');

INSERT INTO Projects (ID, Project_Name, Project_Budget, Employee_Id, Departments_Id) VALUES
    ('P001', 'Web App', 50000.50, 201, 001),
    ('P002', 'API REST', 25000.95, 201, 001),
    ('P003', 'TV Campaign', 30000.45, 202, 002);
INSERT INTO Patients (ID, Patient_Name, Patient_Phone) VALUES
    (501, 'Diana Vargas', '8888-1111'),
    (502, 'Edwin Mora', '8999-2222');

INSERT INTO Specialtys (ID, Specialty_Name) VALUES
    (201, 'Pediatría'),
    (202, 'Cardiología');

INSERT INTO Doctors (ID, Doctor_Name, Specialtys_Id) VALUES
    (401, 'Dr. Soto', 201),
    (402, 'Dr. Mora', 202);

INSERT INTO Appointments(ID, Patients_Id, Doctors_Id, Date, Time) VALUES
    ('A01', 501, 401, '2024-08-01', '10:00AM'),
    ('A02', 501, 401, '2024-08-10', '10:00AM'),
    ('A03', 502, 402, '2024-08-05', '01:00PM');
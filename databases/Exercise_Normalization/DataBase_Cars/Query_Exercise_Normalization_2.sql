INSERT INTO Insurance (ID, Insurance_Company, Insurance_Policy) VALUES
    (001, 'ABC Insurance', 'Fire & Theft'),
    (002, 'XYZ Insurance', 'Full Cover'),
    (003, 'DEF Insurance', 'Collision'),
    (004, 'GHI Insurance', 'Basic Legal');

INSERT INTO Owners (ID, Owner_Name, Owner_Phone) VALUES
    (101, 'Alice Smith', '212-555-0147'),
    (102, 'Bob Johnson', '310-555-0192'),
    (103, 'Claire Brown', '415-555-0138'),
    (104, 'Dave Davis', '202-555-0174'),
    (105, 'David Wilson', '312-555-0115'),
    (106, 'Sarah Taylor', '407-555-0183'),
    (107, 'James Anderson', '214-555-0126'),
    (108, 'Amanda Martinez', '702-555-0169'),
    (109, 'Robert White', '206-555-0151'),
    (110, 'Ashley Harris', '617-555-0198');

INSERT INTO Makes (ID, Make) VALUES
    (001, 'Honda'),
    (002, 'Tesla'),
    (003, 'Toyota'),
    (004, 'Ford'),
    (005, 'Audi'),
    (006, 'Mazda');

INSERT INTO Cars (VIN, Makes_Id, Model, Year, Color) VALUES
    ('1HGCR2F83HA000101', 001, 'Accord', 2017, 'Black'),
    ('JTDKN3DU4A0000106', 003, 'Prius', 2010, 'Silver'),
    ('WA1CBAFP8DA000111', 005, 'A4', 2018, 'Black'),
    ('JTDKN3DU4A0000107', 003, 'Camry', 2019, 'Gray'),
    ('1HGCR2F83HA000102', 001, 'Civic', 2020, 'Blue'),
    ('1HGCR2F83HA000103', 001, 'CR-V', 2022, 'Silver'),
    ('5YJ3E1EA7JF000104', 002, 'Model 3', 2018, 'White'),
    ('JM1GL1U56G1000113', 006, 'Mazda3', 2018, 'Red'),
    ('JM1GL1U56G1000114', 006, 'CX-5', 2020, 'Gray'),
    ('5YJ3E1EA7JF000105', 002, 'Model Y', 2021, 'Red'),
    ('JTDKN3DU4A0000108', 003, 'RAV4', 2021, 'White'),
    ('1FA6P8CF0H5000109', 004, 'Mustang', 2017, 'Red'),
    ('WA1CBAFP8DA000110', 005, 'Q5', 2013, 'Blue'),
    ('JM1GL1U56G1000115', 006, 'CX-90', 2022, 'Blue'),
    ('WA1CBAFP8DA000112', 005, 'A6', 2020, 'White'),
    ('JM1GL1U56G1000116', 006, 'MX-5 Miata', 2019, 'Black');

INSERT INTO Cars_Ownership (ID, Cars_VIN, Owners_Id, Insurance_Id) VALUES
    (1,  '1HGCR2F83HA000101', 101, 001),
    (2,  '1HGCR2F83HA000102', 101, 002),
    (3,  '1HGCR2F83HA000103', 102, 003),
    (4,  '5YJ3E1EA7JF000104', 103, 002),
    (5,  '5YJ3E1EA7JF000105', 103, 002),
    (6,  'JTDKN3DU4A0000106', 104, 004),
    (7,  'JTDKN3DU4A0000107', 105, 001),
    (8,  'JTDKN3DU4A0000108', 105, 003),
    (9,  '1FA6P8CF0H5000109', 106, 001),
    (10, 'WA1CBAFP8DA000110', 107, 002),
    (11, 'WA1CBAFP8DA000111', 107, 003),
    (12, 'WA1CBAFP8DA000112', 108, 004),
    (13, 'JM1GL1U56G1000113', 109, 001),
    (14, 'JM1GL1U56G1000114', 110, 002),
    (15, 'JM1GL1U56G1000115', 110, 003),
    (16, 'JM1GL1U56G1000116', 101, 004);
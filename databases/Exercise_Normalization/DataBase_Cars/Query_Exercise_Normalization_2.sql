INSERT INTO Insurance (ID, Insurance_Company) VALUES
    (501, 'ABC Insurance'),
    (502, 'XYZ Insurance'),
    (503, 'DEF Insurance'),
    (504, 'GHI Insurance');

INSERT INTO Policy (ID, Policy_Type) VALUES
    (401, 'Fire & Theft'),
    (402, 'Full Cover'),
    (403, 'Collision'),
    (404, 'Basic Legal');

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
    (301, 'Honda'),
    (302, 'Tesla'),
    (303, 'Toyota'),
    (304, 'Ford'),
    (305, 'Audi'),
    (306, 'Mazda');

INSERT INTO Models (ID, Makes_Id, Model_Name, Year) VALUES
    (201, 301, 'Accord', 2017),
    (202, 301, 'Civic', 2020),
    (203, 301, 'CR-V', 2022),
    (204, 302, 'Model-3', 2018),
    (205, 302, 'Model Y', 2021),
    (206, 303, 'Prius', 2010),
    (207, 303, 'Camry', 2019),
    (208, 303, 'RAV4', 2021),
    (209, 304, 'Mustang', 2017),
    (210, 305, 'A4', 2018),
    (211, 305, 'Q5', 2013),
    (212, 305, 'A6', 2020),
    (213, 306, 'Mazda3', 2018),
    (214, 306, 'CX-5', 2020),
    (215, 306, 'CX-90', 2024),
    (216, 306, 'MX-5 Miata', 2019);

INSERT INTO Cars (VIN, Models_Id, Color_Type) VALUES
    ('1HGCR2F83HA000101', 201, 'Black'),
    ('JTDKN3DU4A0000106', 206, 'Silver'),
    ('WA1CBAFP8DA000111', 210, 'Black'),
    ('JTDKN3DU4A0000107', 207, 'Gray'),
    ('1HGCR2F83HA000102', 202, 'Blue'),
    ('1HGCR2F83HA000103', 203, 'Silver'),
    ('5YJ3E1EA7JF000104', 204, 'White'),
    ('JM1GL1U56G1000113', 213, 'Red'),
    ('JM1GL1U56G1000114', 214, 'Gray'),
    ('5YJ3E1EA7JF000105', 205, 'Red'),
    ('JTDKN3DU4A0000108', 208, 'White'),
    ('1FA6P8CF0H5000109', 209, 'Red'),
    ('WA1CBAFP8DA000110', 211, 'Blue'),
    ('JM1GL1U56G1000115', 215, 'Blue'),
    ('WA1CBAFP8DA000112', 212, 'White'),
    ('JM1GL1U56G1000116', 216, 'Black');

INSERT INTO Cars_Ownership (ID, Cars_VIN, Owners_Id, Insurance_Id, Policy_Id) VALUES
    (1,  '1HGCR2F83HA000101', 101, 501, 402),
    (2,  '1HGCR2F83HA000102', 101, 502, 401),
    (3,  '1HGCR2F83HA000103', 102, 503, 401),
    (4,  '5YJ3E1EA7JF000104', 103, 502, 404),
    (5,  '5YJ3E1EA7JF000105', 103, 502, 403),
    (6,  'JTDKN3DU4A0000106', 104, 504, 403),
    (7,  'JTDKN3DU4A0000107', 105, 501, 403),
    (8,  'JTDKN3DU4A0000108', 105, 503, 402),
    (9,  '1FA6P8CF0H5000109', 106, 501, 401),
    (10, 'WA1CBAFP8DA000110', 107, 502, 404),
    (11, 'WA1CBAFP8DA000111', 107, 503, 404),
    (12, 'WA1CBAFP8DA000112', 108, 504, 403),
    (13, 'JM1GL1U56G1000113', 109, 501, 402),
    (14, 'JM1GL1U56G1000114', 110, 502, 403),
    (15, 'JM1GL1U56G1000115', 110, 503, 404),
    (16, 'JM1GL1U56G1000116', 101, 504, 402);
INSERT INTO Categories (Id, Name, Description) VALUES
    (1, 'Laptops y Laptops Gamer', 'Equipos portátiles de alto rendimiento para trabajo, estudio y videojuegos.'),
    (2, 'Smartphones y Celulares', 'Teléfonos inteligentes de última generación, accesorios y tecnología móvil.'),
    (3, 'Monitores y Pantallas', 'Monitores de alta definición, pantallas ultra anchas y de nivel profesional.'),
    (4, 'Periféricos y Accesorios', 'Teclados, mouses, alfombrillas y accesorios para potenciar la productividad.'),
    (5, 'Televisores y Video', 'Televisores Smart TV, proyectores y equipos de entretenimiento para el hogar.'),
    (6, 'Audio y Sonido', 'Audífonos con cancelación de ruido, bocinas Bluetooth y barras de sonido.'),
    (7, 'Consolas y Videojuegos', 'Consolas de videojuegos de última generación, mandos y juegos digitales.'),
    (8, 'Tablets y Lectores', 'Dispositivos táctiles portátiles ideales para diseño, lectura y consumo multimedia.'),
    (9, 'Relojes Inteligentes', 'Smartwatches y pulseras de actividad para monitoreo de salud y ejercicio.'),
    (10, 'Almacenamiento Digital', 'Discos duros externos, memorias SSD de alta velocidad y unidades Flash USB.'),
    (11, 'Impresión y Escáners', 'Impresoras láser, multifuncionales e inyección de tinta para oficina y hogar.'),
    (12, 'Fotografía y Video', 'Cámaras profesionales, lentes, trípodes y equipos de iluminación fotográfica.'),
    (13, 'Redes y Conectividad', 'Routers Wi-Fi, conmutadores, repetidores de señal y cables de red de alta velocidad.'),
    (14, 'Componentes de PC', 'Tarjetas de video, procesadores, fuentes de poder y memoria RAM para ensamblar PC.'),
    (15, 'Energía y Protección', 'Reguladores de voltaje, suprensores de picos y unidades UPS para respaldar equipos.');

UPDATE Products SET Category_id = 1 WHERE Id = 1;
UPDATE Products SET Category_id = 2 WHERE Id IN (2, 3);
UPDATE Products SET Category_id = 3 WHERE Id = 4;
UPDATE Products SET Category_id = 4 WHERE Id = 5;
UPDATE Products SET Category_id = 10 WHERE Id = 13;

SELECT *
    FROM Products
    ORDER BY Category_id DESC;
# Fundamentos de Internet 


## 1. Del Cliente al Servidor
**Que hace el cliente (navegador)?**
    El cliente es la aplicación local (Chrome, Firefox, Edge, etc.) que actúa como interfaz del usuario. Cuando presionas Enter: 
    El navegador analiza la URL para identificar el protocolo (https://), el dominio ([www.youtube.com](https://www.youtube.com)) 
    y la ruta solicitada.

    Revisa su caché de DNS local y la del sistema operativo para verificar si ya conoce la dirección de YouTube de una sesión reciente. 
    Si está almacenada, se omite el proceso de búsqueda DNS.

**Que papel cumple el DNS?**
    Si la dirección no está guardada en la caché local, el navegador consulta al servidor DNS (Domain Name System), que actúa como
    la libreta de contactos de Internet:

    El cliente envía un mensaje al DNS Resolver de tu proveedor de red o servicio configurado (ej. 8.8.8.8).

    El resolver realiza una consulta en cascada a los servidores Root (.), de dominio de nivel superior TLD (.com) y finalmente al
    servidor DNS autoritativo de Google.

    El DNS devuelve la dirección numéricamente ruteable correspondiente al nombre de dominio (por ejemplo, 142.250.190.46 o una 
    dirección IPv6).

**Que ocurre con la direccion IP?**
    La Dirección IP identifica de forma única la ubicación lógica del servidor de Google en la red global.

    Enrutamiento IP: Los paquetes de datos viajan a través de múltiples routers en Internet utilizando la IP de destino para guiarse.

    Handshake TCP: El cliente establece una conexión estable con el servidor mediante el protocolo de transporte TCP a través del 
    saludo de tres vías (Three-Way Handshake): envío de SYN, recepción de SYN-ACK y confirmación ACK.

**Que hace el Servidor?**
    Los servidores de YouTube (compuestos por balanceadores de carga, servidores web de aplicaciones y servidores de contenido 
    en la red CDN de Google) reciben la instrucción:

    Validan las credenciales y cookies del usuario.

    Consultan bases de datos para recuperar metadatos del video, recomendaciones y comentarios.

    Generan la respuesta devolviendo un código de estado 200 OK junto con el código HTML, archivos CSS y scripts JavaScript iniciales.

**Como entra en juego el protocolo HTTP/HTTPS?**
    HTTPS (HTTP Secure) define la estructura del mensaje y añade una capa de cifrado mediante TLS/SSL: TLS Handshake: Cliente y servidor 
    intercambian certificados de seguridad y negocian claves de cifrado simétrico para garantizar privacidad e integridad en el canal.

    Solicitud HTTP GET: Una vez cifrado el canal, el cliente envía un encabezado de petición solicitando la página o el video 
    en cuestión:

    GET /watch?v=dQw4w9WgXcQ HTTP/2
    Host: www.youtube.com


## 2. Frontend y Backend en acción
**Indique que parte del sistema corresponderia al frontend y cual al backend?**
*FRONTEND:*
    Es la interfaz gráfica interactiva con la que el paciente o el médico interactúan directamente desde el navegador o dispositivo móvil.

    Responsabilidades en la app de citas:
    Mostrar el formulario para seleccionar especialidad, médico y fecha disponible.
    Capturar los datos del paciente (nombre, correo, motivo de consulta).
    Mostrar confirmaciones visuales, calendarios interactivos y mensajes de error (por ejemplo, si falta llenar un campo).
    
*BACKEND:*
    Es el motor interno que se ejecuta en el servidor. Procesa las reglas de negocio, valida la seguridad y gestiona los datos persistentes.

    Responsabilidades en la app de citas:
    Verificar si el médico realmente tiene libre el horario seleccionado (evitar citas dobles).
    Guardar la cita agendada en la base de datos de manera segura.
    Disparar eventos secundarios, como enviar un correo o SMS de confirmación al paciente.
    Controlar la autenticación de usuarios (pacientes, médicos y administradores).

**Mencione tres tecnologias posibles para cada uno?**
*FRONTEND:*
    React / Vue.js / Angular: Frameworks y librerías de JavaScript que permiten construir la interfaz de usuario de forma modular 
    (por componentes) y reactiva.

    HTML5 / CSS3: La estructura básica del contenido y los estilos visuales que el navegador interpreta para renderizar la página.

    TypeScript / JavaScript: El lenguaje de programación que corre directamente en el navegador del cliente para dar interactividad 
    a la aplicación.

*BACKEND:*
    Node.js / Python / Java: Lenguajes y entornos de ejecución que procesan la lógica de negocio, las reglas del sistema y las peticiones 
    en el servidor.

    Frameworks Web (Express, FastAPI, Django, Spring Boot): Herramientas que facilitan la creación de servidores HTTP y la definición de 
    las rutas para exponer Web APIs.

    Bases de Datos (PostgreSQL, MongoDB, MySQL): Sistemas encargados de almacenar, consultar y gestionar la información de manera 
    persistente.

**Explique brevemente cómo el frontend se comunicaría con el backend (mencione los conceptos de API, HTTP y request/response)?**
    El Frontend y el Backend no están unidos físicamente; se comunican mediante red siguiendo el modelo Cliente-Servidor.

    [ Cliente / Frontend ] ─── Request (POST /api/citas) ───► [ Servidor / Backend ]
    [ Cliente / Frontend ] ◄── Response (201 Created) ────── [ Servidor / Backend ]

    API (Application Programming Interface):
    El Backend expone un conjunto de reglas y puntos de acceso (llamados endpoints, por ejemplo: /api/medicos o /api/agendar-cita). 
    La API REST actúa como el contrato que define qué solicitudes acepta el servidor y en qué formato responderá (habitualmente JSON).

    HTTP (Hypertext Transfer Protocol):
    Es el protocolo de transporte de mensajes a través de la red. Define cómo se formatean las peticiones. Los verbos más comunes 
    utilizados son:
    GET: Para pedir datos (ej. obtener la lista de médicos disponibles).
    POST: Para enviar nuevos datos (ej. crear una nueva cita).
    PUT / PATCH: Para modificar información existente (ej. reprogramar una cita).
    DELETE: Para eliminar un registro (ej. cancelar una cita).

    Request / Response (Petición y Respuesta):
    El Request: Cuando el paciente hace clic en "Confirmar Cita", el Frontend construye una solicitud HTTP de tipo POST hacia la 
    URL de la API, enviando en el cuerpo (body) un objeto JSON con los detalles:
    {
    "paciente_id": 104,
    "medico_id": 12,
    "fecha": "2026-09-15",
    "hora": "10:30"
    }
    El Response: El Backend recibe el Request, procesa la lógica en su base de datos y le devuelve al Frontend una respuesta HTTP 
    con un código de estado (por ejemplo, 201 Created si fue exitoso o 409 Conflict si el horario ya estaba ocupado) y un mensaje 
    con el resultado. El Frontend lee esta respuesta y actualiza la pantalla del paciente acorde al resultado.


## 3. REST vs SOAP vs GraphQL
*|-------------|------------------------|--------------------------|-------------------------------|-----------------------------------|*
*| Tipo de API | Formato de datos usado | Nivel de flexibilidad    | Dificultad de implementación  | Uso actual (Alta / Media / Baja)  |*
*|-------------|------------------------|--------------------------|-------------------------------|-----------------------------------|*
*| REST        | JSON, XML, HTML, TXT   |Media ( EL servidor define|Baja (Curva rápida, estándar   |                                   |*
*|             | (JSON es el estandar)  |los esquemas fijado por   |maduro con amplio soporte)     |             Alta                  |*
*|             |                        |cada endpoint)            |                               |                                   |*
*|-------------|------------------------|--------------------------|-------------------------------|-----------------------------------|*
*| SOAP        |   XML Exclusivamente   |Baja (Estructura rígida   |Alta (Complejo, requiere       |   Baja en desarrollos nuevos;     |*
*|             |                        |mediante contratos        |configuración amplia y soporte |       Alta en desarrollos         |*
*|             |                        |estrictos WSDL)           |de protocolos)                 |        viejos y legados           |*
*|-------------|------------------------|--------------------------|-------------------------------|-----------------------------------|*
*| GraphQL     |          JSON          |Alta (El cliente consulta |Media (Requiere definir        |                                   |*
*|             |                        |y pide únicamente los     |esquemas detallados y          |           Media - Alta            |*
*|             |                        |campos requeridos)        |resolvedores)                  |                                   |*
*|-------------|------------------------|--------------------------|-------------------------------|-----------------------------------|*

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
    Para una startup moderna de reservas en línea, la opción más adecuada es REST (o una arquitectura híbrida centrada en REST con adopción 
    puntual de GraphQL en aplicaciones móviles).

    Razones de la elección:
    Velocidad de desarrollo y Time-to-Market:
    Las startups necesitan validar rápidamente sus productos en el mercado. REST cuenta con ecosistemas avanzados en frameworks modernos 
    (como FastAPI o Django en Python, Express en Node.js, Spring Boot en Java), lo que permite construir y desplegar endpoints funcionales 
    en muy poco tiempo.

    Caché nativa y rendimiento:
    En un sistema de reservas, las consultas de catálogos, ubicaciones o servicios disponibles cambian con relativa frecuencia pero son leídas 
    constantemente. REST aprovecha los mecanismos de caché HTTP estándar (como encabezados Cache-Control y CDN), reduciendo significativamente 
    la carga de los servidores principales sin complejidad adicional.

    Facilidad de integración con terceros:
    Un sistema de reservas en línea suele requerir integraciones externas con pasarelas de pago (Stripe, PayPal), servicios de mensajería 
    (Twilio, SendGrid) o calendarios. Prácticamente todas estas plataformas ofrecen SDKs basados en REST/JSON, simplificando la interoperabilidad.

    Curva de aprendizaje e incorporación de talento:
    Es mucho más rápido incorporar desarrolladores a un proyecto con estándares REST bien documentados (OpenAPI/Swagger) que manejar la 
    complejidad de mantenimiento de esquemas de GraphQL o la rigidez de SOAP.

    Excepción de uso: Si la startup desarrolla principalmente aplicaciones móviles y necesita minimizar el consumo de datos celulares evitando 
    solicitudes repetidas (over-fetching y under-fetching), GraphQL es una alternativa excelente para la capa de la interfaz móvil.


## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:** (https://jsonplaceholder.typicode.com/posts)
- **Descripción:** Esta es una API publica que me permite hacer los diferentes metodos que debemos practicar ya que la API de "pokemon" no
    me permitia hacer los metodos de PUT, POST, PATCH o DELETE solo me permitia hacer GET asi que busque en linea por una API que me lo
    permitiera y encontre la que inclui anteriormente.

### 4.2 Configuración en Postman
- **Nombre de la colección:** CRUD API practice
- **Solicitudes agregadas:** - GET - POST - PUT - PATCH - DELETE -

### 4.3 Ejecución y análisis

    Inclui los archivos siguientes para demostrar las ejecuciones con la collection y el environmental:
    1.- (Testing a new environment-jsonplaceholder.postman_environment.json)
    2.- (CRUD API practice-jsonplaceholder.postman_collection_with_respond.json)

### 4.4 Explicación técnica

#### [Get post]
- **Método HTTP:** GET
- **Endpoint:** WITH ENVIRONMENTAL: {{url_base}}/posts WITHOUT: https://jsonplaceholder.typicode.com/posts
- **Parámetros / body:** None
- **Descripción de la respuesta:** Fue exitosa mandandome un 200

#### [Create post]
- **Método HTTP:** POST
- **Endpoint:** WITH ENVIRONMENTAL: {{url_base}}/posts WITHOUT: https://jsonplaceholder.typicode.com/posts   
- **Parámetros / body:** {
    "title": "New Post Created 2",
    "body": "Content of my second test",
    "userId": 2
    }
- **Descripción de la respuesta:** Fue existosa mandandome un 201

#### [Replace post]
- **Método HTTP:** PUT
- **Endpoint:** WITH ENVIRONMENTAL: {{url_base}}/posts/1 WITHOUT: https://jsonplaceholder.typicode.com/posts/1
- **Parámetros / body:** {
    "id": 1,
    "title": "Fully updated title 2",
    "body": "Text completely replaced 2",
    "userId": 2
    }
- **Descripción de la respuesta:** Fue exitosa mandandome un 200

#### [Update partial title]
- **Método HTTP:** PATCH
- **Endpoint:** WITH ENVIRONMENTAL: {{url_base}}/posts/1 WITHOUT: https://jsonplaceholder.typicode.com/posts/1
- **Parámetros / body:**{
    "title": "Just change the title"
    }
- **Descripción de la respuesta:** Fue exitosa mandandome un 200

#### [Delete post]
- **Método HTTP:** DELETE
- **Endpoint:** WITH ENVIRONMENTAL: {{url_base}}/posts/1 WITHOUT: https://jsonplaceholder.typicode.com/posts/2
- **Parámetros / body:** None
- **Descripción de la respuesta:** Fue exitosa mandandome un 200

**¿Qué aprendiste del proceso?** Que cuando uno quiere trabajar con los diferentes metodos en un ambiente de HTTP que te pide hacer los diferentes
    endpoints para usar la API que va a usar en cuestion nuestro Frontend para comunicarse con el Backend los "Environmental" ayudan mucho para no
    estar siempre recordando la url que tenemos que usar siempre ya que cuando fueramos a trabajar con muchas API lo mejor es resumirlas con un
    environmental y eso resuelve muchas confusiones.

### 4.5 Reflexión final

    Senti toda la practica muy ligera pero con muchos conceptos que aprender y tener que recordar y repasar pero interesantes ya que las API son 
    muy importantes para que sepa como es la plantilla y las firmas en la que la informacion debe ser manejada y ordenada para que la Base de datos
    no se haga un gran desorden y ademas que los conseptos de HTTP y las url como los DNS y las IP que son interpretadas para que cada Dominio 
    pueda ser usado y cada metodo como el CRUD en resumen me da la manera mas facil de interaccion con las API .JSON que debe ser fue muy interesante
    aprender todo esto.
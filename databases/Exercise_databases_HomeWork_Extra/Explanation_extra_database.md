# ¿Cada factura debe tener relación con un usuario, o puede existir una factura sin cuenta?
    Cada factura debe tener relacion con un usuario ya que para que se pueda efectuar una factura es necesario que se
    incluya el Email del usuario, y como vamos a inclur la tabla que contenga la informacion de usuario no se puede
    tener una factura sin Email y por consiguiente sin la informacion del Usuario ya que la estamos ligando la columna
    Buyer_Email con la columna Buyer_Email.
# ¿Necesita una tabla intermedia? ¿Por qué?
    No se necesita una tabla intermedia ya que la nueva columna de Invoices_Buyer_Email es un campo Unique que solo cada
    usuario puede tener un solo y unico email relacionado a cada usuario sin la opcion de duplicados, asi que aunque un 
    usuario puede tener muchas facturas compradas por el mismo usuario cada factura solo puede contener el email de un
    unico usuario por cada factura realizada haciendo una relacion de 1:N de la tabla Users con la tabla Invoces.
# ¿Ahora se relaciona mediante el id del usuario, ¿es necesario mantener el correo del usuario como en el ejercicio anterior?
    No mas bien debe eliminarse ya que buscando informacion me di cuenta que no lo puedo apreciar al 100% en la aplicacion
    de "DrawSQL" que aunque graficamente yo vea campos creados con los nombres y sus tipo en realidad en codigo yo creo las
    relaciones y lo que cada tabla puede recibir eso quiere decir que en realidad debo eliminar los campos de "Buyer_Email"
    en las dos tablas "Invoices" y "Shopping Cart" para reemplazarlas con la FK Users_ID para cada tabla y dentro en el 
    codigo debo de crear la relacion que de esa FK con la relacion a su PK solo reciban el Buyer_Email que es un campo
    "Unique" en la tabla "Users".
# ¿Una reseña puede existir sin un producto o sin un usuario?
    NO podria existir ya que como creamos una relacion con la tabla de Products y de Users le estamos diciendo a Reviews que
    cada review tiene que estar relacionada con un User y un Product para que pueda existir haciendo que las relaciones esten
    de 1:N teniendo 1 de las dos tablas Products y Users a N con la tabla Reviews teniendo que 1 Producto puede tener varios
    reviews y 1 usuario puede tener hechos varios reviews.
# ¿Cada factura debe tener exactamente un método de pago, o podría haber más de uno?
    Una Factura en efecto puede tener varios metodods de pago porque un cliente puede tener que acompletar para pagar una
    factura en su totalidad con varios tipos de pago haciendo que un factura pueda tener varios tipos de pagos haciendo 
    que tengamos una relacion N:M por ese motivo es muy necesario crear una tabla intermedia para crear esa relacion ya que
    la tabla Payment Method puede mandarle varios a la tabla Invoices haciendo que Invoices no pueda recibir en su columna
    multiples tipos de pagos asi que creamos una tabla intermendia llamada "Invoice Payment" para completar la relacion
    N:M.

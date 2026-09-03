# s = 'abracadabra'
# count = {}
# for ch in s:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1
# keys = sorted(count.keys())
# for k in keys:
#     print(f"{k}:{count[k]}", end=" ")


# for i in range(2):
#     for j in range(2):
#         print(i+j, end="")


# nums= [2, 4, 6, 8]
# result= []
# for n in nums:
#     if n % 4 == 0:
#         result.append(n//2)
#     else:
#         result.append(n+1)
# print(result)


# nums = [1, 2, 3, 4, 5, 6]
# result = []
# for i in range(len(nums)):
#     if i % 2 == 0:
#         result.append(nums[i] * 2)
#     else:
#         result.append(nums[i] + 3)
# # result = result[::-1]
# result.reverse()
# print(result)


# print(bool("False"))


# def manual_add(n):
#     result = 0
#     for i in range(1, n + 1):
#         result += i
#     return result
# def add_formula(n):
#     return n * (n + 1) // 2

# number=add_formula(50)
# print(number)


# a = [1,2,3]
# print(len(a))


# data = {
#     "JavaScript" : 3,
#     "React" : 2,
#     "SQL" : 4
# }
# result = []
# for language, count in data.items():
#     for number in range(count):
#         result.append(language[:number+1])
# result = sorted(
#     result,
#     key=len,
#     reverse=True
# )
# print(result)


# import asyncio
# import datetime
# async def asyncHello(name: str, seconds: int):
#     print(f"""the function{name}, last {seconds} seconds
#         starts in {datetime.datetime.now().strftime('%H:%M:%S')}""")
#     await asyncio.sleep(seconds)
#     print(
#         f"the function {name} has ended in {datetime.datetime.now().strftime('%H:%M:%S')}")
# asyncio.run(asyncHello("Test", 5))
# async def extra_exercises():
#     await asyncio.gather(
#         asyncHello("C", 3),
#         asyncHello("B", 2),
#         asyncHello("A", 1),
#     )
# asyncio.run(extra_exercises())


# x = 10
# try:
#     x = x/0
# except ZeroDivisionError:
#     print("error ocurred")
# print (x)


# import FreeSimpleGUI as sg

# counter = 0

# layout = [
#     [sg.Text("Haz click en lo que quieras hacer")],
#     [sg.Text(counter, key="-COUNTER-")],
#     # Añadimos un segundo botón en la misma fila (misma lista)
#     [sg.Button("Sumar"), sg.Button("Restar"), sg.Button("close")],
# ]

# window = sg.Window("Primer programa", layout)

# while True:
#     event, values = window.read()
    
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == "Sumar":
#         counter += 1
#     elif event == "Restar":
#         counter -= 1
#     elif event == "close":
#         break

#     # Refrescamos la pantalla con el nuevo valor
#     window["-COUNTER-"].update(counter)

# window.close()



# import FreeSimpleGUI as sg


# def mostrar_segunda_pantalla():
#     # Diseño de la nueva ventana
#     layout_secundario = [
#         [sg.Text("¡Esta es la nueva pantalla!")],
#         [sg.Button("Cerrar")],
#     ]

#     # Crear la nueva ventana
#     ventana_2 = sg.Window("Segunda Ventana", layout_secundario)

#     # Bucle de la nueva ventana
#     while True:
#         evento_2, valores_2 = ventana_2.read()
#         if evento_2 == sg.WIN_CLOSED or evento_2 == "Cerrar":
#             break

#     ventana_2.close()


# # Diseño de la ventana principal
# layout_principal = [
#     [sg.Text("Ventana Principal")],
#     [sg.Button("Abrir Nueva Pantalla")],
#     [sg.Button("Salir")],
# ]

# ventana_1 = sg.Window("Principal", layout_principal)

# # Bucle principal
# while True:
#     evento, valores = ventana_1.read()

#     if evento == sg.WIN_CLOSED or evento == "Salir":
#         break

#     # Mandar llamar la función al presionar el botón
#     if evento == "Abrir Nueva Pantalla":
#         mostrar_segunda_pantalla()

# ventana_1.close()



# import FreeSimpleGUI as sg

# # Definimos el diseño de la ventana
# layout = [
#     [sg.Text("Selecciona una fecha:")],
#     # El campo de entrada donde se escribirá la fecha seleccionada
#     [sg.Input(key="-FECHA-", size=(20, 1)), 
#     # El botón que abre el calendario apuntando al "target" (su caja de texto)
#     sg.CalendarButton("Abrir Calendario", target="-FECHA-", format="%Y-%m-%d", close_when_date_chosen=True)],
#     [sg.Button("Enviar"), sg.Button("Salir")]
# ]

# window = sg.Window("Selector de Fechas", layout)

# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, "Salir"):
#         break
#     if event == "Enviar":
#         # Leemos el valor guardado automáticamente en el Input
#         sg.popup(f"Has seleccionado la fecha: {values['-FECHA-']}")

# window.close()



# import FreeSimpleGUI as sg

# layout = [
#     [sg.Text('Selecciona una fecha:')],
#     # El calendario escribirá el string en este Input
#     [sg.Input(key='-FECHA-', size=(20, 1))], 
#     # Usamos 'format' para pedir solo Día/Mes/Año
#     [sg.CalendarButton('Abrir Calendario', target='-FECHA-', format='%d-%m-%Y')],
#     [sg.Button('OK')]
# ]

# window = sg.Window('Ejemplo Calendario', layout)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'OK':
#         print("El valor recibido es un string:", values['-FECHA-'])
#         break

# window.close()



# import FreeSimpleGUI as sg

# # 1. Definir el diseño de la ventana
# layout = [
#     [sg.Text("¿Cuál es tu lenguaje favorito?")],
#     # Ambos pertenecen al grupo "LANG"
#     [sg.Radio("Python", "LANG", default=True, key="-PYTHON-"), 
#     sg.Radio("JavaScript", "LANG", key="-JS-")],
#     [sg.Button("Enviar"), sg.Button("Salir")]
# ]

# # 2. Crear la ventana
# window = sg.Window("Ejemplo de Radio Buttons", layout)

# # 3. Bucle de eventos
# while True:
#     event, values = window.read()
    
#     if event in (sg.WIN_CLOSED, "Salir"):
#         break
        
#     if event == "Enviar":
#         # values[key] devuelve True si está seleccionado o False si no lo está
#         if values["-PYTHON-"]:
#             sg.popup("¡Excelente elección! Elegiste Python.")
#         elif values["-JS-"]:
#             sg.popup("¡Genial! Elegiste JavaScript.")

# window.close()



# import FreeSimpleGUI as sg

# layout = [
#     [sg.Text("¡Texto que cambia de color!", font=("Arial", 16), key="-TEXTO-")],
#     # Al poner enable_events=True, el input generará un evento al recibir el color
#     [sg.Input(key="-INPUT_COLOR-", enable_events=True, visible=True), 
#     sg.ColorChooserButton("Elegir Color", target="-INPUT_COLOR-")]
# ]

# window = sg.Window("Demo Interactiva", layout)

# while True:
#     event, values = window.read()
    
#     if event == sg.WIN_CLOSED:
#         break
        
#     # Cuando el input cambia su contenido gracias al ColorChooserButton
#     if event == "-INPUT_COLOR-":
#         color_elegido = values["-INPUT_COLOR-"]
#         # Evitamos errores si el usuario cierra el selector sin elegir nada
#         if color_elegido and color_elegido != "None": 
#             window["-TEXTO-"].update(text_color=color_elegido)

# window.close()






# import FreeSimpleGUI as sg

# # Lista donde guardaremos las categorías como diccionarios
# lista_categorias = []

# layout = [
#     [sg.Text("Nombre de la Categoría:"), sg.Input(key="-NOMBRE-", size=(20, 1))],
    
#     # Este input recibirá el código del color directamente desde el botón
#     [sg.Text("Color seleccionado:"), 
#     sg.Input(key="-COLOR-", size=(10, 1), readonly=True), # readonly evita que escriban cosas raras
#     sg.ColorChooserButton("Elegir Color", target="-COLOR-")],
    
#     [sg.Button("Salvar Categoría"), sg.Button("Salir")],
    
#     [sg.Text("Categorías Guardadas:")],
#     [sg.Listbox(values=[], size=(40, 6), key="-LISTA_VISUAL-")]
# ]

# window = sg.Window("Gestor de Categorías", layout)

# while True:
#     event, values = window.read()
    
#     if event in (sg.WIN_CLOSED, "Salir"):
#         break
        
#     if event == "Salvar Categoría":
#         nombre = values["-NOMBRE-"].strip()
#         color = values["-COLOR-"]
        
#         # Validaciones básicas
#         if not nombre:
#             sg.popup_error("Por favor, introduce un nombre para la categoría.")
#             continue
#         if not color or color == "None":
#             sg.popup_error("Por favor, selecciona un color para la categoría.")
#             continue
            
#         # Guardamos la categoría en nuestra lista de datos
#         nueva_categoria = {"nombre": nombre, "color": color}
#         lista_categorias.append(nueva_categoria)
        
#         # Actualizamos la lista visual para mostrar el resultado (Nombre + Hexadecimal)
#         nombres_visibles = [f"{c['nombre']} ({c['color']})" for c in lista_categorias]
#         window["-LISTA_VISUAL-"].update(values=nombres_visibles)
        
#         # Limpiamos los campos para la siguiente categoría
#         window["-NOMBRE-"].update("")
#         window["-COLOR-"].update("")

# window.close()

# # Al final, tu lista de datos queda perfectamente estructurada así:
# print("Lista final guardada:", lista_categorias)



# import FreeSimpleGUI as sg

# # 1. Tu diccionario original con los colores Hex
# colores_por_categoria = {
#     'petexpenses': '#FF0000',  # Letra Roja
#     'food': '#008000',         # Letra Verde
#     'utilities': '#0000FF'    # Letra Azul
# }

# # 2. Los datos que irán dentro de tu tabla (Matriz de datos)
# datos_tabla = [
#     ['01/03/2026', 'Alimento perro', 'petexpenses', '$50'],
#     ['02/03/2026', 'Supermercado', 'food', '$100'],
#     ['03/03/2026', 'Luz eléctrica', 'utilities', '$45'],
#     ['04/03/2026', 'Juguete gato', 'petexpenses', '$15']
# ]

# # 3. Procesamos los datos para crear la lista de tuplas que sg.Table necesita
# configuracion_colores = []

# for indice, fila in enumerate(datos_tabla):
#     categoria = fila[2]  # Supongamos que la categoría está en la columna índice 2
    
#     if categoria in colores_por_categoria:
#         color_hex_texto = colores_por_categoria[categoria]
#         # Estructura: (Índice, Color Texto, Color Fondo)
#         # Usamos el color de fondo por defecto de la tabla o uno de tu agrado (ej. 'white')
#         configuracion_colores.append((indice, color_hex_texto, '#FFFFFF'))

# # 4. Diseño de la ventana de PySimpleGUI
# layout = [
#     [sg.Table(values=datos_tabla,
#         headings=['Fecha', 'Detalle', 'Categoría', 'Monto'],
#         row_colors=configuracion_colores, # <-- Aquí se asignan los colores inicialmente
#         key='-TABLA-',
#         auto_size_columns=True,
#         num_rows=10)],
#     [sg.Button('Cambiar colores dinámicamente'), sg.Button('Salir')]
# ]

# window = sg.Window('Ejemplo de Colores en Tabla', layout)

# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Salir'):
#         break
        
#     # Si necesitas actualizar los colores en tiempo de ejecución:
#     if event == 'Cambiar colores dinámicamente':
#         # Nuevos colores que quieras aplicar siguiendo la misma lógica de índices
#         nuevos_colores = [
#             (0, '#000000', '#FFD700'), # Fila 0: Texto negro, Fondo Oro
#             (3, '#FFFFFF', '#000000')  # Fila 3: Texto blanco, Fondo Negro
#         ]
#         # Actualizamos usando el método .update() del elemento
#         window['-TABLA-'].update(row_colors=nuevos_colores)

# window.close()




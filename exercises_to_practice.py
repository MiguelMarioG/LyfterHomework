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



import FreeSimpleGUI as sg

# 1. Definir el diseño de la ventana
layout = [
    [sg.Text("¿Cuál es tu lenguaje favorito?")],
    # Ambos pertenecen al grupo "LANG"
    [sg.Radio("Python", "LANG", default=True, key="-PYTHON-"), 
    sg.Radio("JavaScript", "LANG", key="-JS-")],
    [sg.Button("Enviar"), sg.Button("Salir")]
]

# 2. Crear la ventana
window = sg.Window("Ejemplo de Radio Buttons", layout)

# 3. Bucle de eventos
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, "Salir"):
        break
        
    if event == "Enviar":
        # values[key] devuelve True si está seleccionado o False si no lo está
        if values["-PYTHON-"]:
            sg.popup("¡Excelente elección! Elegiste Python.")
        elif values["-JS-"]:
            sg.popup("¡Genial! Elegiste JavaScript.")

window.close()

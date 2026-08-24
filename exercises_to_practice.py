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


import FreeSimpleGUI as sg

counter = 0

layout = [
    [sg.Text("Haz click en lo que quieras hacer")],
    [sg.Text(counter, key="-COUNTER-")],
    # Añadimos un segundo botón en la misma fila (misma lista)
    [sg.Button("Sumar"), sg.Button("Restar"), sg.Button("close")],
]

window = sg.Window("Primer programa", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == "Sumar":
        counter += 1
    elif event == "Restar":
        counter -= 1
    elif event == "close":
        break

    # Refrescamos la pantalla con el nuevo valor
    window["-COUNTER-"].update(counter)

window.close()
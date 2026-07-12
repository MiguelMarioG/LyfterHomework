employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

order_department = {}

for index in employees:
    department = index ["department"]
    if department in order_department:
        order_department[department].append(index)
    else:
        order_department[department] = [index]

print(order_department)
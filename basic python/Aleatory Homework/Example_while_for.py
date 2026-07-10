counter = 1

# El ciclo se ejecutará mientras contador sea menor a 5
while counter <= 5:
    print(f"El contador va por {counter}")

    # Incrementamos el contador para que la condición eventualmente sea False
    counter += 1
print("¡El while ha terminado!")

print()


list_of_car_brands = ["Mercedes Benz" , "Toyota" , "Mazda" , "Hyundai"]

# Por cada elemento en la lista, ejecutamos el bloque

for car_brand in  list_of_car_brands:

    print(f"Ejecutando ciclo para marca: {car_brand}")

print("¡Ciclo completado!")

print()

for number in range (1000000):

    print(f"Número: {number + 1}")
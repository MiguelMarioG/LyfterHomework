#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_list = [24, 33, 13, 44, 20, 5, 9, 12]
new_list = []

for index in my_list:
    if(index % 2 == 0):
        new_list.append(index)

print(new_list)

#sobrepense mucho las cosas usando la funcion .remove sin pensar que uan lista
#nueva solucionaria las cosas al agregarele los enteros gracias por
#la sugerencia y la aclaracion
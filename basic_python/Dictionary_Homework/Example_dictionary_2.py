list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

new_dictionary = {}

for index in range(len(list_a)):
    new_dictionary[list_a[index]] = list_b[index]

print(new_dictionary)
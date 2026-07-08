number_comparison = []

for index in range(0, 10):
    number = int(input(f"Enter number for your list:"))
    number_comparison.append(number)

biggest_number = number_comparison[0]

for index in number_comparison:
    if index >= biggest_number:
        biggest_number = index
    

print(number_comparison)
print(f'The biggest number was: {biggest_number}')
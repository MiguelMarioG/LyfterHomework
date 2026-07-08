smallest_number = []

for index in range(0, 5):
    numbers = int(input(f"Enter number for your list:"))
    smallest_number.append(numbers)

small_number = smallest_number[0]

for index in smallest_number:
    if(index < small_number):
        small_number = index
print()
print(smallest_number)
print (f"the smallest number is: {small_number}")

average_numbers = []
target_numbers = []
number_total = 0
counter = 0

for index in range(0, 5):
    numbers = int(input(f"Enter 5 number for your list:"))
    average_numbers.append(numbers)
    number_total += numbers
    counter += 1

average = number_total / counter

for index in average_numbers:
    if(average < index):
        target_numbers.append (index) 

print()
print(f"Average: {average}")
print(target_numbers)
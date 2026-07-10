my_list = []
count = 0

for index in range(0, 5):
    number = int(input(f"Enter 5 number for your list:"))
    my_list.append(number)
print()
search_number = int(input("Enter the number you want to search: "))

for index in my_list:
    if(index == search_number):
        count += 1

print()
print(my_list)
print(f"the number {search_number} appears {count} times")

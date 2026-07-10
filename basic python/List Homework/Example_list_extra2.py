#my_list = [3, 6, 0, -18, 0, -32, -6, 18]
my_list = []

for index in range(0, 5):
    number = int(input(f"Enter 5 number for your list:"))
    my_list.append(number)

for index in my_list:
    if(index <= 0):
        print("You have at least one negative number or 0")
        break
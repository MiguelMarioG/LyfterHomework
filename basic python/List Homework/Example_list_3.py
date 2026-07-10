my_list = [53, 4, 3, 6, 1, 7, 4, 2, 54, 84, 12]
first_val = 0
last_val = len (my_list) -1

for index, value in enumerate(my_list):
    if(index == first_val):
        temp = value
    elif(index == last_val):
        my_list[first_val] = value
        my_list[last_val] = temp


print(my_list)
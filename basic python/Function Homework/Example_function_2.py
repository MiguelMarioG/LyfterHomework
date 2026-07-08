def example_function ():
    number = 5
    variable = 8
    total_sum = number + variable
    global_total_sum = global_number + global_variable
    print(global_total_sum)
    return total_sum

global_number = 5
global_variable = 10
global_total_sum = 50

sum = example_function()
print (sum)

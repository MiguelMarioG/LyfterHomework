def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])

list_one = [15,24,64,71,20,21,33,10,8,10,11,77,99]
print_10_or_less_elements(list_one)

# Based on this code, and in terms of Big O notation, the complexity is:

#* Time Complexity = O(1)
#* Space Complexity = O(1)

# This is because the list is iterated over only once, and there is a 
# fixed limit—in this case, "10".

# Regarding memory usage, we are only using variables that execute 
# without being modified based on the size "n" of the lists, 
# resulting in O(1) complexity.


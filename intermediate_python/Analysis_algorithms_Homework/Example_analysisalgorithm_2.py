def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

list = [3,5,23,12,10,7]
print_numbers_times_2(list)

# Based on this code, and in terms of Big O notation, it is:

#* Time Complexity = O(n)
#* Space Complexity = O(1)

# This is because there is a "FOR" loop iterating through
# the numbers in a given list—processing each of the "n" 
# numbers—where each number is multiplied by 2 and the 
# result is printed.

# In terms of in-memory processing—specifically processing
# a single list without copying or implementing anything 
# extra—the notation is O(1).
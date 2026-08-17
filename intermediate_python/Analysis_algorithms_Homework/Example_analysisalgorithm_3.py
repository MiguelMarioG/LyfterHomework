def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:                   
		for element_b in list_b:                   
			if element_a == element_b:
				return True
				
	return False

list_one = [2, 3, 1, 5, 8, 9]
list_two = [3, 4, 5, 0, 9, 1]
print(check_if_lists_have_an_equal(list_one, list_two))

# Based on this code, and in terms of Big O notation, the complexity is:

#* Time Complexity = O(n²)
#* Space Complexity = O(1)

# This is because there are two iterations—implemented via nested "FOR" 
# loops—that compare one list against the other to check for matching elements.

# Regarding memory usage, the notation is O(1) because we are dealing 
# with two interacting lists previously created and send it to the Function.
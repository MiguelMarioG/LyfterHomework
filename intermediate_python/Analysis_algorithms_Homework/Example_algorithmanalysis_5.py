def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

list_one = [2, 5, 1, 8, 23, 45, 13, 10]
list_two = [4, 11, 33, 98, 56, 88, 24, 99]
list_three = [51, 55, 64, 18, 66, 30, 9, 1]

generated = generate_list_trios(list_one, list_two, list_three)
print(generated)

# Based on this code, and in terms of Big O notation, the complexity is:

#* Time Complexity = O(n³)
#* Space Complexity = O(n³)

# This is O(n³) notation because we are implementing three nested "FOR" 
# loops to iterate over the three lists received by the function, 
# resulting in longer processing time since each value must be processed 
# "n" times for each loop.

# Regarding space complexity, we are looking at O(n³); this is because, 
# while we utilize the three lists passed to the function, we create one 
# additional list to store all the sets generated during the iterations 
# over those three lists.
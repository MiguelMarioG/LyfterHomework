def bubble_sort_ascending(list_to_sort):
	for first_index in range(0, len(list_to_sort) - 1):
		has_made_change = False
		for index in range(0, len(list_to_sort) - 1 - first_index):       
			current_element = list_to_sort[index]
			next_element = list_to_sort[index + 1]
			print(f'-- iteration {first_index + 1}, {index + 1}. Actual Element: {current_element}, Next Element: {next_element}')
			if current_element > next_element:             
				print('-- The current element is greater than the next one. Swapping them...')
				list_to_sort[index] = next_element
				list_to_sort[index + 1] = current_element
				has_made_change = True
			else:
				print('-- The current element is smaller than the next one. Nothing change...')
		if not has_made_change:
			return

# Based on this code, and in terms of Big O notation, the complexity is:

#* Time Complexity = O(n²)
#* Space Complexity = O(1)

# This is because the first `for` loop involves searching for each element based
# on the list's length, followed by comparisons between elements to perform the sorting.

# Consequently, the complexity is O(n²) because it employs a nested iteration—two `FOR`
# loops to process the elements of a single list, resulting in a longer execution time
# that scales with the length of the list.

# In terms of in-memory processing—specifically processing a single list without copying
# or implementing anything extra—the notation is O(1).
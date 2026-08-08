def bubble_sort_validate(list_to_validate):
	for element in list_to_validate:
		if element == None or isinstance(element, str):
			return True
	return False


def bubble_sort(list_to_validate):
	if bubble_sort_validate(list_to_validate):
		raise TypeError ("The list contains non-numeric elements")
	
	for first_index in range(0, len(list_to_validate) - 1):
		has_made_change=False
		for index in range(0, len(list_to_validate) - 1 - first_index):
			current_element = list_to_validate[index]
			next_element = list_to_validate[index + 1]

			print(f'-- iteration {first_index + 1}, {index + 1}. Actual Element: {current_element}, Next Element: {next_element}')

			if current_element > next_element:
				print('-- The current element is greater than the next one. Swapping them...')
				list_to_validate[index] = next_element
				list_to_validate[index + 1] = current_element
				has_made_change = True
			else:
				print('-- The current element is smaller than the next one. Nothing change...')
		if not has_made_change:
			return


# list_sort = [2, 5, 1, 3, 4, 6]
# bubble_sort(list_sort)
# print (list_sort)

# second_list_sort = [51,46,11,34,88,92,70,27,66,152]
# bubble_sort(second_list_sort)
# print(second_list_sort)

list_to_validate = [5, "hello", 2]
bubble_sort(list_to_validate)
print(list_to_validate)






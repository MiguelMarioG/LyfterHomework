def bubble_sort_validate(list_to_validate):
	if not list_to_validate:
		return "Error: The list is empty"
	for element in list_to_validate:
		if isinstance(element, bool) or not isinstance(element, (int, float)):
			return "Error: The List contain non-numeric elements"
	return None


def bubble_sort(list_to_validate):
	error_message = bubble_sort_validate(list_to_validate)
	if error_message:
		print(error_message)
		return error_message
	
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
			break


# list_sort = [2, 5, 1, 3, 4, 6]
# bubble_sort(list_sort)
# print (list_sort)

# second_list_sort = [51,46,11,34,88,92,70,27,66,152]
# bubble_sort(second_list_sort)
# print(second_list_sort)

list_to_validate = [5, "hello", 2]
bubble_sort(list_to_validate)

# list_to_validate = []
# bubble_sort(list_to_validate)





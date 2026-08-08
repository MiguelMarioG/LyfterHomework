def bubble_sort_steps(list_to_sort):
	has_made_change = 0
	iteration = 0
	
	for first_index in range(0, len(list_to_sort) - 1):
		iteration += 1

		for index in range(0, len(list_to_sort) - 1 - first_index):
			current_element = list_to_sort[index]
			next_element = list_to_sort[index + 1]

			print(f'-- iteration {first_index + 1}, {index + 1}. Actual Element: {current_element}, Next Element: {next_element}')

			if current_element > next_element:
				print('-- The current element is greater than the next one. Swapping them...')
				list_to_sort[index] = next_element
				list_to_sort[index + 1] = current_element
				has_made_change += 1
			else:
				print('-- The current element is smaller than the next one. Nothing change...')
		if not has_made_change:
			return
	print(f"Iterations: {iteration}")
	print(f"Exchanges: {has_made_change}")

list_sort = [2, 5, 1, 3, 4, 6]
bubble_sort_steps(list_sort)
print (list_sort)

second_list_sort = [51,46,11,34,88,92,70,27,66,152]
bubble_sort_steps(second_list_sort)
print(second_list_sort)
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


def bubble_sort_descending(list_to_sort):
	for first_index in range(0, len(list_to_sort) - 1):

		has_made_change = False

		for index in range(0, len(list_to_sort) - 1 - first_index):
			current_element = list_to_sort[index]
			next_element = list_to_sort[index + 1]

			print(f'-- iteration {first_index + 1}, {index + 1}. Actual Element: {current_element}, Next Element: {next_element}')

			if current_element < next_element:
				print('-- The current element is smaller than the next one. Swapping them...')
				list_to_sort[index] = next_element
				list_to_sort[index + 1] = current_element
				has_made_change = True
			else:
				print('-- The current element is greater than the next one. Nothing change...')
		if not has_made_change:
			return


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort_ascending(my_test_list)
print(my_test_list)

print()

my_second_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort_descending(my_second_test_list)
print(my_second_test_list)

print()

my_third_test_list = [12, 3, 5, 11, 9, 3, 7, 13, 18, 11, 10]
bubble_sort_ascending(my_third_test_list)
print(my_third_test_list)





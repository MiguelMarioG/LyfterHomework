def bubble_sort_validate(list_to_validate):
	if not isinstance(list_to_validate, list):
		raise TypeError("Values ​​that are not a list cannot be used")

	elif not list_to_validate:
		raise ValueError("The list is empty")

	for element in list_to_validate:
		if isinstance(element, bool) or not isinstance(element, (int, float)):
			raise ValueError("The list contain invalid values")
		
	return True


def bubble_sort(list_to_validate):
	bubble_sort_validate(list_to_validate)

	for first_index in range(0, len(list_to_validate) - 1):
		has_made_change=False

		for index in range(0, len(list_to_validate) - 1 - first_index):
			current_element = list_to_validate[index]
			next_element = list_to_validate[index + 1]

			if current_element > next_element:
				list_to_validate[index] = next_element
				list_to_validate[index + 1] = current_element
				has_made_change = True

		if not has_made_change:
			break

	return list_to_validate
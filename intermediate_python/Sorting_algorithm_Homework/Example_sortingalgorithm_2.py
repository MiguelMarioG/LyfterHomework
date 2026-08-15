def bubble_sort_backward(list_to_sort):
    for first_index in range(0, len(list_to_sort) -1):
        has_made_any_change = False
        count = 1
        for index in range(len(list_to_sort) -1, first_index, -1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index-1]
            print(f'-- iteration {first_index + 1}, {count}. Actual Element: {current_element}, Next Element: {next_element}')
            count += 1
            if current_element < next_element:
                print('-- The current element is smaller than the next one. Swapping them...')
                list_to_sort[index] = next_element
                list_to_sort[index - 1] = current_element
                has_made_any_change = True
            else:
                print('-- The current element is greater than the next one. Nothing change...')
        if not has_made_any_change:
            return

my_test_list = [12, 3, 5, 11, 9, 3, 7, 13, 18, 11, 10]
bubble_sort_backward(my_test_list)
print(my_test_list)

print()

my_second_list = [1, 2, 3, 4, 10, 5, 6, 7, 8, 9]
bubble_sort_backward(my_second_list)
print(my_second_list)



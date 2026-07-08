def remove_tenths(numbers_list):
    index = 0
    while (index < len(numbers_list)):
        if numbers_list[index] % 10 == 0:
            numbers_list.pop(index)
        else:
            index += 1


def multiply_numbers_by_2(numbers_list):
    for index, number in enumerate(numbers_list):
        numbers_list[index] = number * 2


def main():
    numbers_list = [53, 60, 32, 62, 400, 10]
    remove_tenths(numbers_list)
    multiply_numbers_by_2(numbers_list)
    print(numbers_list)


if __name__ == "__main__":
    main()
def get_numbers ():
    number_list = []
    counter = "y"
    while counter == "y":
        print("------------Program count numbers------------")
        number_list.append(int(input("Enter your number: ")))
        counter = (input("Do you want to enter another number (y or n): "))
    return number_list


def sum_list (sum_numbers):
    if not sum_numbers:
        raise ValueError("You cannot sum an empty list")

    total_sum_numbers = sum(sum_numbers)

    if any(isinstance(num, float) for num in sum_numbers):
        return round(float(total_sum_numbers), 2)

    return total_sum_numbers


def main():
    numbers = get_numbers()
    total = sum_list(numbers)
    print(total)


if __name__ == "__main__":
    main()
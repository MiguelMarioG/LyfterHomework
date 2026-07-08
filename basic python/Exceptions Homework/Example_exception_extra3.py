def sum_values_list (combined_list):
    sum_total = 0
    for index, value in enumerate (combined_list):
        try:
            combined_list[index] = float (value)
            sum_total += combined_list[index]
            print(f'{combined_list[index]} "added up correctly')
        except ValueError as error:
            print (f'"Invalid element: {combined_list[index]}", {error}')
    return sum_total


def main():
    combined_list = ["10", "apple", "5.5", "3", "n/a"]
    grand_total = sum_values_list (combined_list)
    print(f'"Grand Total of the sum: {grand_total}')


if __name__ == "__main__":
    main()


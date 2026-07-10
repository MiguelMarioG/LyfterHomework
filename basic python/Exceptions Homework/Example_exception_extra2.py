def convert_to_int (combined_list):
    print("Result:")
    for index, value in enumerate (combined_list):
        try:
            combined_list[index] = int (value)
            print(f'"{value}" "converted into" {combined_list[index]}')
        except ValueError as error:
            print (f'"Could not convert the item: {combined_list[index]}", {error}')


def main():
    combined_list = ["4", "hola", "10", "5.2"]
    convert_to_int (combined_list)


if __name__ == "__main__":
    main()


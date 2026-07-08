def word_backwards(my_string):
    word_length = len(my_string)
    char = ""
    for index in range (word_length - 1, -1, -1):
        char += my_string[index]
    return (char)


def main():
    my_string = input("Introduce your Word: ")
    string_char = word_backwards(my_string)
    print(string_char)


if __name__ == "__main__":
    main()

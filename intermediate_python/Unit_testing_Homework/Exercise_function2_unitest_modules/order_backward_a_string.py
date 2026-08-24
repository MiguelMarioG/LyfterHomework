def word_backwards(my_string):
    if not my_string:
        raise ValueError ("Error: your variable is empty")
    inverted_char = my_string [:: -1]
    return (inverted_char)


def main():
    my_string = input("Introduce your Word: ")
    string_char = word_backwards(my_string)
    print(string_char)


if __name__ == "__main__":
    main()

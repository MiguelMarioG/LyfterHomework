def separate_word (string_word):
    if not string_word:
        raise ValueError("Error: It is an empty value")
    
    new_word = string_word.split("-")

    for index in new_word:
        if not index:
            raise ValueError("Error: cannot split empty values")
    return (new_word)


def sort_word (word_to_sort):
    word_to_sort.sort(key=str.lower)
    sorted_word = "-".join(word_to_sort)
    return sorted_word


def main ():
    string_word =  "computer-airplane-function-monitor-train-python-variable-zion"
    word_to_sort = separate_word (string_word)
    result = sort_word(word_to_sort)
    print(result)


if __name__ == "__main__":
    main()
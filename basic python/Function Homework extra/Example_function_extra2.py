def define_words ():
    list_word = []
    for index in range(0, 5):
        word = input(f"Enter your words:")
        list_word.append(word)
    return list_word


def size_based_number (list_word):
    string_larger = []
    number = int(input("Enter the length of the word: "))
    for word in list_word:
        if len(word) > number:
            string_larger.append (word)
    return string_larger


def main():
    list_word = define_words()
    larger_words = size_based_number(list_word)
    if larger_words:
        print (f"Your longer words are: {larger_words}")
    else:
        print ("You don't have any word longer than your number")


if __name__ == "__main__":
    main()


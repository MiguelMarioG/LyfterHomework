def get_words (string_word, letter):
    counter = 0
    for index in string_word:
        if index == letter:
            counter += 1
    return counter


def main():
    string_word = input ("Enter your word: ")
    letter = input ("Enter your character you want to search: ")
    times_in_word =get_words (string_word, letter)
    print (f"the times your letter: {letter} appears is: {times_in_word} times")


if __name__ == "__main__":
    main()
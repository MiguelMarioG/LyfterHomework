def define_vowel(string_word):
    counter=0
    string_vowel="aeiouAEIOU"
    for vowel in string_word:
        if vowel in string_vowel:
            counter+=1
    return counter


def main():
    string_word=input("Enter your word: ")
    quantity_vowel=define_vowel(string_word)
    print(f"The number of vowels in your word is {quantity_vowel}")


if __name__ == "__main__":
    main()
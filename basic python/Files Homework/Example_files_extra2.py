def creating_book (path, book_sample):
    with open(path, "w", encoding="utf-8") as file:
        file.write(book_sample)


def counting_word_book (path):
    counter = 0
    with open(path, "r", encoding="utf-8") as file:
        book_words = file.read()
        word_counting = book_words.split()
        counter = len(word_counting)
    return counter


def main():
    book_sample = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.\n" \
    "However little known the feelings or views of such a man may be on his first entering a neighborhood,\n" \
    "this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters."

    creating_book("book_a_tale_of_romance.txt", book_sample)
    number_of_words = counting_word_book("book_a_tale_of_romance.txt")
    print(f'"this file contain:" {number_of_words} "words"')


if __name__ == "__main__":
    main()


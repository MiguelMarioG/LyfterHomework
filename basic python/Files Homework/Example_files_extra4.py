def append_file(path, new_word):
    with open(path, "a", encoding="utf-8") as file:
        file.write("\n" + new_word)


def read_file (path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
    
def main ():
    new_word = input("Enter your word: ")
    file_name = input("Enter your file name: ") + ".txt"
    append_file(file_name, new_word)
    file_with_added_words = read_file(file_name)
    print(file_with_added_words)


if __name__ == "__main__":
    main()



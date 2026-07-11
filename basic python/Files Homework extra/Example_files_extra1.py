def read_new_file(path):
    with open(path, "r", encoding="utf-8") as file:
        new_word = file.readlines()
    return new_word


def ordered_file_words(ordered_word):
    clean = (line.strip() for line in ordered_word) 
    ordered_word = " ".join(clean)
    print()
    print(ordered_word)
    return ordered_word


def write_new_file_ordered (ordered_word):
    file_name = input("Enter your file name: ") + ".txt"
    with open (file_name, "w", encoding="utf-8") as file:
        file.write(ordered_word)


def read_file_by_lines(path, new_word):   
    for line in new_word:
        print(f"{line.strip()}")
    w_ordered = ordered_file_words(new_word)
    write_new_file_ordered (w_ordered)


def main():
    new_word = read_new_file("hello_world_python.txt")
    read_file_by_lines("hello_world_python.txt", new_word)


if __name__ == "__main__":
    main()



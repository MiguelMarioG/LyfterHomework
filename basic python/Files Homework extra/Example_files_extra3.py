def read_words (path):
    with open(path, "r", encoding="utf-8") as file:
        all_words = file.read()
        print(all_words)
        upper_words = all_words.upper()
    return(upper_words)


def create_upper_words (path, words):
    with open(path, "w", encoding="utf-8") as file:
        file.write(words)
        print()
        print(words)


def main ():
    upper_words = read_words("hello_world_python.txt")        #Aqui estoy usando un archivo que ya cree en el ejercicio 1
    create_upper_words("HELLO_WORLD_PYTHONS.txt", upper_words)


if __name__ == "__main__":
    main()


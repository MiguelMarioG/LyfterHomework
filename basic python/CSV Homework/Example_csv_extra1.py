import csv

def read_videogame (path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for videogame_number, videogame in enumerate (reader, start=1):
            print(f"Your Video Game #{videogame_number}")
            for head, row in videogame.items():
                print(f"{head} : {row}")
            print()


def main():
    file_name = input("Enter the name of the file you want to open: ") + ".csv"
    sep_final = read_videogame (file_name)
    print(sep_final)


if __name__ == "__main__":
    main()


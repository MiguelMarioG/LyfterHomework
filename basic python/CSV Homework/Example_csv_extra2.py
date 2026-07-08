import csv

def read_videogame (path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list (reader)


def videogame_classification (reader, option):
        count = 1
        for series in reader:
            if option == series["Classification ESRB"]:
                print(f"The Videogame #{count} with the classification {option} is")
                for head, row in series.items():
                    print(f"{head} : {row}")
                count += 1
                print()


def main ():
    file_name = input("Enter the name of the file you want to open: ") + ".csv"
    option = input("Enter the classification of your videogame: ")
    print()
    reader = read_videogame (file_name)
    videogame_classification(reader, option)


if __name__ == "__main__":
    main()



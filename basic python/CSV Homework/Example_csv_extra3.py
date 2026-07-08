import csv

def gender_count (path):
    gender_counts = {}
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for index in reader:
            gender = index["Gender"]
            if gender not in gender_counts:
                gender_counts[gender] = 0
            gender_counts[gender] += 1
    return gender_counts     


def gender_print (gender_count):
    print("--------------Genders found it--------------")
    for gender, count in sorted(gender_count.items()):
        print(f"{gender}: {count}")


def main():
    dictionary_gender = gender_count ("video_games.csv")
    gender_print(dictionary_gender)


if __name__ == "__main__":
    main()




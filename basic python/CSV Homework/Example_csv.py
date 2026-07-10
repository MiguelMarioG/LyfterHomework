import csv

def read_series(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for series in reader:
            print(f"Top choice: {series['Name']} on {series['Platform']} - Score: {series['Score']}/10.")

        #for shows in reader:
        #    print(shows)

read_series("top_series.csv")
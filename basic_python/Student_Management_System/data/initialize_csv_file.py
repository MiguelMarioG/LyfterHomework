import csv
import os


def save_data_to_csv (path, student_full_data):
    if not student_full_data:
        print("There is no data in memory to save on file")
        print()
        return
    
    headers = [
        "full name", "section",
        "spanish grade", "english grade",
        "social grade", "sciences grade"
        ]

    with open (path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for (name, section), info in student_full_data.items():
            row = {
                "full name": name,
                "section" : section,
                "spanish grade" : info["spanish grade"],
                "english grade" : info["english grade"],
                "social grade" : info["social grade"],
                "sciences grade" : info["sciences grade"]
            }
            writer.writerow(row)
    print(f'Data successfully saved to the file "{path}"!!!')
    print()


def load_data_from_csv (path, student_full_data):
    if not os.path.exists(path):
        print(f'The File "{path}" was not found. Cannot Load the data')
        print()
        return False
    
    with open (path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            name = row["full name"].strip()
            section = row["section"].strip()

            key = (name, section)

            student_full_data[key] = {
                "spanish grade" : int(row["spanish grade"]),
                "english grade" : int(row["section"]),
                "social grade" : int(row["social grade"],),
                "sciences grade" : int(row["sciences grade"])
            }
            count =+ 1
    print(f'Successfully Loaded {count} students from "{path}" into memory!')
    print()
    return True
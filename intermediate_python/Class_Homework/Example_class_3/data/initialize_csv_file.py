import csv
import os
from actions.manage_student_info import Student


def save_data_to_csv (path, student_full_data):
    if not student_full_data:
        print("There is no data in memory to save on file")
        print()
        return
    
    headers = [
        "full name", 
        "section",
        "spanish grade", 
        "english grade",
        "social grade", 
        "sciences grade"
        ]

    with open (path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for student in student_full_data.values():
            row = {
                "full name": student.name,
                "section" : student.section,
                "spanish grade" : student.spanish_g,
                "english grade" : student.english_g,
                "social grade" : student.social_g,
                "sciences grade" : student.sciences_g
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

            student_obj = Student(
                name=name,
                section=section,
                spanish_g=int(row["spanish grade"]),
                english_g=int(row["english grade"]),
                social_g=int(row["social grade"]),
                sciences_g=int(row["sciences grade"]),
            )

            student_full_data[key] = student_obj
            count += 1
    print(f'Successfully Loaded {count} Students from "{path}" into memory!')
    print()
    return True






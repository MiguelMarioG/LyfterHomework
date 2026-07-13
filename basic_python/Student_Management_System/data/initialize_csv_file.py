import csv
import os


def file_exist_to_verify_name_or_section(path):
    file_exists = os.path.exists(path)
    return file_exists    


def verify_csv_exist(path):
    file_exists = os.path.exists(path)
    if not file_exists:
        print(f"The File '{path}' not found. choose option #1 to create new data")
    return file_exists


def append_student_to_csv(path, student_data):
    file_exists = os.path.exists(path)
    with open(path, 'a', encoding='utf-8', newline="") as file:
        headers = student_data.keys() 
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            print(f"The File '{path}' not found. Creating a new file with headers")
            writer.writeheader()   
        writer.writerow(student_data)
        print("Student information saved successfully!")


def reading_csv_created(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        student_list = list(reader)   
    return student_list
import csv


def delete_student_data(path):
    print("=======================Delete Student Information=======================")
    print("========================================================================")
    name = asking_student_name()
    section = asking_student_section()
    students_to_keep = []
    student_found_it = False
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for student in reader:
            csv_name = student["full name"].strip().lower()
            csv_section = student["section"].strip().upper()
            if csv_name == name.strip().lower() and csv_section == section.strip().upper():
                student_found_it = True
                continue
            students_to_keep.append(student)
    if student_found_it:
        with open(path, "w", encoding="utf-8", newline="")as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_to_keep)
        print(f"Student '{name}' with Section '{section}' successfully deleted!")
        print()
    else:
        print("Error: Student not found with that name and section.")
        print()


def name_and_section_duplicated(path, name, section):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_name = row["full name"].strip().lower()
            csv_section = row["section"].strip().upper()
            if csv_name == name.strip().lower() and csv_section == section.strip().upper():
                return True
        return False


def asking_student_name ():
    while True:
        student_name = input ("Enter your Full name: ").strip()
        if not student_name:
            print("You enter a invalid entry on your Full name, please try again")
            print("=============================================================")
            continue
        if any(char.isdigit() for char in student_name):
            print("You enter a invalid entry on your Full name, please try again")
            print("=============================================================")
            continue                
        return student_name


def asking_student_section ():
    while True:
        student_section = input ("Enter your Section: ").strip()
        if not student_section:
            print("You enter a incorrect value on the Section you must enter in the correct order Example:(11B), please try again")
            print("==============================================================================================================")
            continue
        if len(student_section) != 3: 
            print("You enter a incorrect value on the Section you must enter in the correct order Example:(11B), please try again")
            print("==============================================================================================================")
            continue  
        if not (student_section[0:2].isdigit() and student_section[2].isalpha()):
            print("You enter a incorrect value on the Section you must enter in the correct order Example:(11B), please try again")
            print("==============================================================================================================")
            continue                
        return student_section.upper()


def asking_spanish_grades ():
    while True:
        try:
            grade_of_spanish = int(input("Enter the Grade of your Spanish Class: "))
            if grade_of_spanish < 0 or grade_of_spanish > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100), please try again")
                print("========================================================================================================")
                continue
            return grade_of_spanish
        except ValueError as error:
            print(f"You must enter a valid entry on your Spanish Grade, ValueError {error}")


def asking_english_grades ():
    while True:
        try:
            grade_of_english = int(input("Enter the Grade of your English Class: "))
            if grade_of_english < 0 or grade_of_english > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100), please try again")
                print("========================================================================================================")
                continue
            return grade_of_english
        except ValueError as error:
            print(f"You must enter a valid entry on your English Grade, ValueError {error}")


def asking_social_grades ():
    while True:
        try:
            grade_of_social = int(input("Enter the Grade of your Social Class: "))
            if grade_of_social < 0 or grade_of_social > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100), please try again")
                print("========================================================================================================")
                continue
            return grade_of_social
        except ValueError as error:
            print(f"You must enter a valid entry on your Social Grade, ValueError {error}")


def asking_sciences_grades ():
    while True:
        try:
            grade_of_sciences = int(input("Enter the Grade of your Sciences Class: "))
            if grade_of_sciences < 0 or grade_of_sciences > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100), please try again")
                print("========================================================================================================")
                continue
            return grade_of_sciences
        except ValueError as error:
            print(f"You must enter a valid entry on your Sciences Grade, ValueError {error}")


def creating_student_data (path):
    print("===================Student Information Menu===================")
    print("==============================================================")
    while True:
        name = asking_student_name()
        section = asking_student_section()
        if name_and_section_duplicated (path, name, section):
            print()
            print("Error: Your Student Name or Section already exist, try again")
            print("Going back to the Main Menu")
            print("============================================================")
            return False
        break

    spanish_g = asking_spanish_grades()
    english_g = asking_english_grades()
    social_g = asking_social_grades()
    sciences_g = asking_sciences_grades()

    student_data = {
        "full name" : name,
        "section" : section,
        "spanish grade" : spanish_g,
        "english grade" : english_g,
        "social grade" : social_g,
        "sciences grade" : sciences_g
    }
    return student_data


def print_data_csv(read_data):
    print("===============All your Students in the System===============")
    print("=============================================================")
    for index, students in enumerate (read_data, start=1):
        print(f"Your Student #{index} data is: ")
        for head, row in students.items():
            print(f"{head}: {row}")
        print()


def average_students(student_data):
    students = []
    for student in student_data:
        spanish = int(student["spanish grade"])
        english = int(student["english grade"])
        social = int(student["social grade"])
        science = int(student["sciences grade"])
        average = (spanish+english+social+science)/4
        students.append([student["full name"], average])  
    return students


def top_3_students(student_data, top_students ):
    print("====================Top 3 Students Overall===================")
    print("=============================================================")
    if not student_data:
        print("No student data found on your student file")
        print("==========================================")
        return
    top_students.sort(key=lambda x: x[1], reverse=True)
    top_three = top_students[:3]
    for index, student_info in enumerate(top_three, start=1):
        name = student_info[0]
        avg = student_info[1]
        print(f"Top #{index}: {name} with Average of: {avg}")
    print()


def average_all_students(student_data, average_data):
    print("=======================Students Overall======================")
    print("=============================================================")
    if not student_data:
        print("No student data found on your student file")
        print("==========================================")
    count = 0
    all_average = 0
    for index, students in enumerate (average_data, start=1):
        name = students[0]
        average = students[1]
        all_average += average
        count += 1
        print(f"Your Student #{index} {name}: Average is {average}")
    print()
    total_average = all_average/ count
    print(f"The total Average of All Students is: {total_average}")
    print()


def failing_students_report(student_data):
    print("===================Failing Students Report===================")
    print("=============================================================")
    any_failing_student = False
    failing_score = 60 
    for student in student_data:
        failed_subjects = []
        if int(student["spanish grade"]) < failing_score:
            failed_subjects.append(f"Spanish ({student['spanish grade']})")
            
        if int(student["english grade"]) < failing_score:
            failed_subjects.append(f"English ({student['english grade']})")
            
        if int(student["social grade"]) < failing_score:
            failed_subjects.append(f"Social Studies ({student['social grade']})")
            
        if int(student["sciences grade"]) < failing_score:
            failed_subjects.append(f"Sciences ({student['sciences grade']})")

        if failed_subjects:
            any_failing_student = True
            print(f"Student: {student['full name']} with Section: {student['section']}")
            print(f"Failing in: {', '.join(failed_subjects)}")
            print("=================================================================")

    if not any_failing_student:
        print("Excellent! There are no failing students in the system")
        print("======================================================")
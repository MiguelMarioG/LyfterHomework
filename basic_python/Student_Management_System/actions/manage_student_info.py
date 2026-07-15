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


def creating_student_data (student_full_data):
    print("===================Student Information Menu===================")
    print("==============================================================")
    while True:
        name = asking_student_name()
        section = asking_student_section()

        if (name, section) in student_full_data:
            print()
            print("Error: Your Student Name and Section already exist, try again")
            print("Going back to the Main Menu")
            print("============================================================")
            print()
            return False
        break
        
    spanish_g = asking_spanish_grades()
    english_g = asking_english_grades()
    social_g = asking_social_grades()
    sciences_g = asking_sciences_grades()

    student_full_data[(name, section)] = {
        "spanish grade" : spanish_g,
        "english grade" : english_g,
        "social grade" : social_g,
        "sciences grade" : sciences_g
    }

    print("Your Student data is added to local memory successfully")
    print()
    return True


def delete_student_data(student_full_data):
    print("=======================Delete Student Information=======================")
    print("========================================================================")
    name = asking_student_name()
    section = asking_student_section()

    key = (name, section)

    if key in student_full_data:
        del student_full_data[key]
        print(f"Student '{name}' with Section '{section}' successfully deleted!")
        print()
    else:
        print("Error: Student not found in memory with that name and section.")
        print()


def print_data_csv(student_full_data):
    print("===============All your Students in the Memory===============")
    print("=============================================================")

    if not student_full_data:
        print("No Student data available in memory")
        print()
        return

    for index, ((name, section), info) in enumerate(student_full_data.items(), start=1):
        print(f"Your Student #{index} data is: ")
        print(f"full name: {name}")
        print(f"section: {section}")
        for subject, grade in info.items():
            print(f"{subject}: {grade}")
        print()


def average_students(student_full_data):
    students = []
    for (name, section), info in student_full_data.items():
        avg = (info["spanish grade"] + info["english grade"] + info["social grade"] + info["sciences grade"]) / 4
        students.append([name, avg])
    return students


def top_3_students(average_data):
    print("====================Top 3 Students Overall===================")
    print("=============================================================")
    if not average_data:
        print("No student data found in your memory")
        print("====================================")
        print()
        return

    top_students = sorted(average_data, key=lambda x: x[1], reverse=True)
    for index, student_info in enumerate(top_students[:3], start=1):
        print(f"Top #{index}: {student_info[0]} with Average of: {student_info[1]:.2f}")
    print()


def average_all_students(average_data):
    print("=======================Students Overall======================")
    print("=============================================================")
    if not average_data:
        print("No student data found in your memory")
        print("====================================")
        print()
        return
    
    total_average = 0
    for index, student in enumerate(average_data, start=1):
        print(f"Your Student #{index} {student[0]}: Average is {student[1]:.2f}")
        total_average += student[1]
    print()
    print(f"\nThe total Average of All Students is: {(total_average / len(average_data)):.2f}\n")
    print()


def failing_students_report(student_full_data):
    print("===================Failing Students Report===================")
    print("=============================================================")
    any_failing_student = False
    failing_score = 60 

    for (name, section), info in student_full_data.items():
        failed_subjects = []
        for subject, grade in info.items():
            if grade < failing_score:
                failed_subjects.append(f"{subject.capitalize()} ({grade})")

        if failed_subjects:
            any_failing_student = True
            print(f"Student: {name} with Section: {section}")
            print(f"Failing in: {', '.join(failed_subjects)}")
            print("=================================================================")
            print()

    if not any_failing_student:
        print("Excellent! There are no failing students in the system")
        print("======================================================")
        print()
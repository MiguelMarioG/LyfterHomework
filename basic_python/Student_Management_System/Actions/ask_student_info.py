def asking_student_name ():
    while True:
        try:
            student_name = print ("Enter your Full name: ")
            if student_name == " ":
                print("You enter a invalid entry on your Full name")
                print("===========================================")
                continue
            return student_name
        except ValueError as error:
            print(f"You must enter a valid entry on your name, ValueError {error}")


def asking_student_section ():
    while True:
        try:
            student_section = print("Enter your Section: ")
            if student_section and not student_section[0].isdigit():
                print("You enter a incorrect value on the Section you must enter in the correct order Example:(11B)")
                print("==============================================================================")
                continue
            return student_section
        except ValueError as error:
            print(f"You must enter a valid entry on your section, ValueError {error}")


def asking_spanish_grades ():
    while True:
        try:
            grade_of_spanish = int(input("Enter the Grade of your Spanish Class: "))
            if grade_of_spanish < 0 and grade_of_spanish > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100)")
                print("============================================================================")
                continue
            return grade_of_spanish
        except ValueError as error:
            print(f"You must enter a valid entry on your Spanish Grade, ValueError {error}")


def asking_english_grades ():
    while True:
        try:
            grade_of_english = int(input("Enter the Grade of your English Class: "))
            if grade_of_english < 0 and grade_of_english > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100)")
                print("============================================================================")
                continue
            return grade_of_english
        except ValueError as error:
            print(f"You must enter a valid entry on your English Grade, ValueError {error}")


def asking_social_grades ():
    while True:
        try:
            grade_of_social = int(input("Enter the Grade of your Social Class: "))
            if grade_of_social < 0 and grade_of_social > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100)")
                print("============================================================================")
                continue
            return grade_of_social
        except ValueError as error:
            print(f"You must enter a valid entry on your Social Grade, ValueError {error}")


def asking_sciences_grades ():
    while True:
        try:
            grade_of_sciences = int(input("Enter the Grade of your Sciences Class: "))
            if grade_of_sciences < 0 and grade_of_sciences > 100:
                print("You enter a invalid value on your Grade, your grade must be on this criteria (0 - 100)")
                print("============================================================================")
                continue
            return grade_of_sciences
        except ValueError as error:
            print(f"You must enter a valid entry on your Sciences Grade, ValueError {error}")

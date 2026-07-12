from System_Menus.Menu import student_system_menu, student_information_menu
from Actions.ask_student_info import asking_student_name, asking_student_section, asking_spanish_grades, asking_english_grades, asking_social_grades, asking_sciences_grades


def main ():
    student_option = student_system_menu()
    if student_option == 1:
        print("============Student Information============")
        student_information_menu


if __name__ == "__main__":
    main()
from system_menus.menu_student import (
    student_system_menu,
    asking_csv_name,
    student_information_menu
)
from actions.manage_student_info import (
    creating_student_data,
    top_3_students,
    average_students,
    average_all_students,
    delete_student_data,
    failing_students_report,
    print_data_csv
)
from data.initialize_csv_file import (
    save_data_to_csv,
    load_data_from_csv
)


def main ():
    student_full_data = {}

    while True:
        student_option = student_system_menu()

        if student_option == 1:
            choice = True
            while choice:
                success = creating_student_data(student_full_data)
                if not success:
                    break
                choice = student_information_menu()

        elif student_option == 2:
            print_data_csv(student_full_data)

        elif student_option == 3:
            avg_data = average_students(student_full_data)
            top_3_students(avg_data)

        elif student_option == 4:
            avg_data = average_students(student_full_data)
            average_all_students(avg_data)

        elif student_option == 5:
            delete_student_data(student_full_data)

        elif student_option == 6:      
            failing_students_report(student_full_data)

        elif student_option == 7:
            path_file = asking_csv_name()
            load_data_from_csv(path_file, student_full_data)

        elif student_option == 8:
            path_file = asking_csv_name()
            save_data_to_csv(path_file, student_full_data)

        elif student_option == 9:
            print("Exiting the system. Goodbye!")
            break


if __name__ == "__main__":
    main()






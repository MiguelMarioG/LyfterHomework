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
    append_student_to_csv,
    file_exist_to_verify_name_or_section,
    verify_csv_exist,
    reading_csv_created
)


def main ():
    path = asking_csv_name()
    while True:
        student_option = student_system_menu()
        if student_option == 1:
            choice = True
            while choice:
                verify = file_exist_to_verify_name_or_section(path)
                if verify == True:
                    student_data = creating_student_data(path)
                    if student_data == False:
                        break
                    append_student_to_csv(path, student_data)
                    choice = student_information_menu()
                continue
        elif student_option == 2:
            verify = verify_csv_exist(path)
            if verify == True:
                read_data = reading_csv_created(path)
                print_data_csv(read_data)
            continue
        elif student_option == 3:
            verify = verify_csv_exist(path)
            if verify == True:
                read_data = reading_csv_created(path)
                average_data = average_students(read_data)
                top_3_students(read_data, average_data)
            continue
        elif student_option == 4:
            verify = verify_csv_exist(path)
            if verify == True:
                read_data = reading_csv_created(path)
                average_data = average_students(read_data)
                average_all_students(read_data, average_data)
            continue
        elif student_option == 5:
            verify = verify_csv_exist(path)
            if verify == True:
                delete_student_data(path)
        elif student_option == 6:
            verify = verify_csv_exist(path)
            if verify == True:      
                read_data = reading_csv_created(path)
                failing_students_report(read_data)  
        elif student_option == 7:
            break


if __name__ == "__main__":
    main()
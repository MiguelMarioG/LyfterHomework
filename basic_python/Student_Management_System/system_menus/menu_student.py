def student_system_menu ():  
        print("===================Student System Menu===================")
        print("=========================================================")
        print("1.- Enter the Student's Information")                      
        print("2.- View all the Student's Information")                    
        print("3.- See the Top 3 Student's Overall")                      
        print("4.- Average Grade of each Student")  
        print("5.- Delete a Student Information")  
        print("6.- Failing Students Report")                     
        print("7.- Exit")                                                  
        print("=========================================================")
        try:
            option = int(input("Enter your option: "))
            print()
            if option <= 0 or option > 7:
                print("Invalid option try again with a valid option (1 - 7)")
                print("====================================================")
            return option
        except ValueError as error:
            print(f"You must enter a valid number (1 - 7). Letters or symbols are not allowed. ValueError {error}")
            print("======================================================================================")


def student_information_menu ():
    while True:
        answer = input("Do you want to add a Student Information (y or n): ")
        print()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print('Invalid option, please enter "y" for Yes or "n" for No')


def asking_csv_name():
    print("===============initializing your system file================")
    print("============================================================")
    csv_name = input ("Enter your file name for initialization: ").strip() + ".csv"
    print()
    return csv_name
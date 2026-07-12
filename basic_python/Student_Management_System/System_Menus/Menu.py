def student_system_menu ():
    while True:    
        print("===================Student System Menu===================")
        print("=========================================================")
        print("1.- Enter the Student's Information")                      
        print("2.- View all the Student's Information")                    
        print("3.- See the Top 3 Student's Overall")                      
        print("4.- Average Grade of each Student")                         
        print("5.- Exit")                                                  
        print("=========================================================")

        try:
            option = int(input("Enter your option: "))
            if option <= 0 or option > 5:
                print("Invalid option try again with a valid option (1 - 5)")
                print("====================================================")
                continue
            return option
        except ValueError as error:
            print(f"You must enter a valid number (1 - 5). Letters or symbols are not allowed. ValueError {error}")
            print("======================================================================================")
    return option


def student_information_menu ():
    while True:
        print("===================Student Information Menu===================")
        print("==============================================================")

        try:
            answer = input("Do you want to enter a Student Information (y or n): ")
            if answer == "y":
                return True
            elif answer == "n":
                return False
        except ValueError as error:
            print('Invalid option, please enter "y" for Yes or "n" for No')
            



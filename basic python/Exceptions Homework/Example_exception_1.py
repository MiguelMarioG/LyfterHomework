actual_number = 15

def calculator_addition():
    global actual_number
    try:
        print()
        print("-----------------Option #1 Addition------------------")
        print("-----------------------------------------------------")    
        new_number = int(input("Enter the new number for the Addition: "))
        actual_number = new_number + actual_number
        print(f"Your total is: {actual_number}")
    except ValueError as error:
        print(f"An error occurred while trying to add a string to an int {error}")


def calculator_subtraction():
    global actual_number
    try:
        print()
        print("----------------Option #2 Subtraction----------------")
        print("-----------------------------------------------------")    
        new_number = int(input("Enter the new number for the Subtraction: "))
        actual_number = actual_number - new_number
        print(f"Your total is: {actual_number}")
    except ValueError as error:
        print(f"An error occurred while trying to add a string to an int {error}")


def calculator_multiplication():
    global actual_number
    try:
        print()
        print("--------------Option #3 Multiplication---------------")
        print("-----------------------------------------------------")    
        new_number = int(input("Enter the new number for the Multiplication: "))
        actual_number = new_number * actual_number
        print(f"Your total is: {actual_number}")
    except ValueError as error:
        print(f"An error occurred while trying to add a string to an int {error}")


def calculator_division():
    global actual_number
    try:
        print()
        print("-----------------Option #4 Division------------------")
        print("-----------------------------------------------------")    
        new_number = float(input("Enter the new number for the Division: "))
        actual_number = actual_number / new_number
        print(f"Your total is: {actual_number}")
    except ZeroDivisionError as error:
        print(f"Action taken: Cannot divide by zero. Defaulting result to 0.")


def calculator_clear_result():
    global actual_number
    print()
    print("---------------Option #5 Clear Result----------------")
    print("-----------------------------------------------------")
    print(f"Your total result {actual_number} now is clear")
    actual_number = 0  


def menu_calculator ():
    try:
        print()
        print("-------------Your Python calculator menu-------------")
        print("-----------------------------------------------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear result")
        print()
        option = int (input("Enter your option: "))
        return (option)
    except Exception as error:
        print(f"The Value you enter is incorrect {error}")


def calculator_exit():
    try:
        print()
        exit_program = (input("Do you want to choose another option on your menu (y or n): "))
        if exit_program != "y" and exit_program != "n":
            raise ValueError ("You enter a invalid option")
        return exit_program
    except Exception as error:
        print(f"The Value you enter is incorrect {error}")


def main ():
    exit_program = "y" 
    while exit_program == "y":
        calculator_option = menu_calculator()
        if calculator_option == 1:
            calculator_addition()
            exit_program = calculator_exit()
        elif calculator_option == 2:
            calculator_subtraction()
            exit_program = calculator_exit()
        elif calculator_option == 3:
            calculator_multiplication()
            exit_program = calculator_exit()
        elif calculator_option == 4:
            calculator_division()
            exit_program = calculator_exit()
        elif calculator_option == 5:
            calculator_clear_result()
            exit_program = calculator_exit()


if __name__ == "__main__":
    main()
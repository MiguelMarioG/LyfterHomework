class MathOperation:
    def __init__(self, first_number, second_number):
        if first_number is None or first_number == "":
            raise ValueError("You must to enter a integer value")
        if second_number is None or second_number == "":
            raise ValueError("You must to enter a integer value")
        try:
            self.first_number = int(first_number)
            self.second_number = int (second_number)
        except ValueError:
            raise TypeError ("Error: String variables cannot be divided")


    def addition (self):
        return self.first_number + self.second_number


    def subtraction (self):
        return self.first_number - self.second_number


    def multiplication (self):
        return self.first_number * self.second_number


    def divide (self):
        if self.second_number == 0:
            raise ValueError ("You cannot divide by zero")
        result = self.first_number / self.second_number
        return result


def main ():
    first_value = (input("Enter your first number: "))
    second_value = (input("Enter your second number: "))
    operation = MathOperation(first_value, second_value)

    result1 = operation.addition()
    print(result1)

    result2 = operation.subtraction()
    print(result2)

    result3 = operation.multiplication()
    print(result3)

    result4 = operation.divide()
    print(result4)


if __name__ == "__main__":
    main()



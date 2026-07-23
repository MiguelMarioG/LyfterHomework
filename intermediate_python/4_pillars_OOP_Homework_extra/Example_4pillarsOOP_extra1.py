class Employee:
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name  

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("The salary cannot be negative")
        self.__salary = new_salary  

    def promote(self, percentage: float):
        if percentage <= 0:
            print("The percentage must be greater than 0")
            return
        increase = self.__salary * (percentage / 100)
        self.__salary += increase
        print(f"¡{self.__name} Was Promoted! the New Salary: ${self.__salary:,.2f}")


def main():
    employee = Employee("Carlos", 3000.0)
    print(f"Employee: {employee.name} with Salary: ${employee.salary:,.2f}\n")  
    employee.promote(10)  

    #Example if I put a negative Value, can be removed after you check the code
    try:
        employee.salary = -500.0
    except ValueError as error:
        print(f"Error detected: {error}")  


if __name__=="__main__":
    main()


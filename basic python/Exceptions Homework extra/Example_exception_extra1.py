def check_name (name_string):
    if name_string.isdigit():
        raise Exception ("Your name can't have number")


def check_age (age_number):
    if not age_number.isdigit():
        raise Exception ("You enter a invalid number")


def main():
    name_string = input("Enter your name: ")
    try:
        check_name (name_string)
    except Exception as error:
        print(f"Your value is error {error}")

    age_number = input("Enter your age: ")
    try:
        check_age (age_number)
    except Exception as error:
        print(f"Your value is error {error}")

    print(f"Hello {name_string}, your age is {age_number}")


if __name__ == "__main__":
    main()


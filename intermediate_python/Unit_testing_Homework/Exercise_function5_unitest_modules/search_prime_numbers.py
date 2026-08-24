def enter_numbers():
    list_numbers = []
    counter = 0
    while counter < 10:
        number = input("Enter your numbers: ")
        if not number:
            raise ValueError("Error you dont enter a value to check")
        enter_number = int(number)
        list_numbers.append (enter_number) 
        counter += 1
    return (list_numbers)


def define_prime_number (numbers):
    if numbers <= 1:
        return False
    for index in range (2, int(numbers ** 0.5) +1):
        if numbers % index == 0:            
            return False
    return True


def prime_numbers (my_numbers):
    prime_list = []
    for index in my_numbers:
        if define_prime_number(index) == True:
            prime_list.append(index)
    if not prime_list:
        return ("No prime number was found")
    return (prime_list)


def main():
    my_numbers = enter_numbers ()
    result = prime_numbers (my_numbers)
    print(result)


if __name__ == "__main__":
    main()



def count_lower_and_upper(my_string: str) -> str:
    lower_letter = 0
    upper_letter = 0
    if not my_string:
        raise ValueError("Error: cannot count a null value")
    for index in my_string:
        if index.islower():
            lower_letter += 1
        elif index.isupper():
            upper_letter += 1
    return (f"There's {upper_letter} upper cases and {lower_letter} lower cases")

def main ():
    my_string = input("Introduce your Word: ")
    result_counting = count_lower_and_upper(my_string)
    print (result_counting)

if __name__=="__main__":
    main()
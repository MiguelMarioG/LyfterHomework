def word_backwards():
    my_string = input("Introduce your Word: ")
    lower_letter = 0
    upper_letter = 0
    for index in my_string:
        if index.islower():
            lower_letter += 1
        elif index.isupper():
            upper_letter += 1
    print(f"There's {upper_letter} upper cases and {lower_letter} lower cases")

word_backwards()


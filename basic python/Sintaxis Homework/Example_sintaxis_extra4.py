number_one = int (input("enter your first number: "))
print()
number_two = int (input("enter your second number: "))
print()
number_three = int (input("Enter your third number: "))
print()
if (number_one == 30 or number_two == 30 or number_three == 30):
    print("that's correct you got a number 30")
elif (number_one + number_two + number_three == 30):
    print(f"correct the numbers {number_one} + {number_two} + {number_three} = 30")
else:
    print("There is no 30, and their sum doesn't add up to 30 either.")
#elif(number_one, number_two, number_three != 30 and number_one + number_two + number_three !=30):
#    print("There is no 30, and their sum doesn't add up to 30 either.")
number_one = int (input("Enter your first number: "))
number_two = int (input("Enter your second number: "))
number_three = int (input("Enter your third number: "))

if(number_one > number_two and number_one > number_three):
    print(f"your number {number_one} is the Biggest of all of them")
elif(number_two > number_one and number_two > number_three):
    print(f"your number {number_two} is the Biggest of all of them")
else : 
    print(f"your number {number_three} is the Biggest of all of them")
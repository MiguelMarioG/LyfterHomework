import random
secret_number = 0
random_number = random.randint(1, 10)


while(secret_number != random_number):
    secret_number = int(input("Enter your guessing number: "))
else:
    print(f"Congratulation your number {secret_number} is the same as the random number {random_number}")
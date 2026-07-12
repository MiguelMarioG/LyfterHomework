user_name = input("Type your name here: ")
user_lastname = input("Type your last name here: ")
user_age = int(input("Type your Age: "))

if (user_age <= 1):
    print(f"{user_name} you're a beautiful Baby")
elif (user_age <= 10):
    print(f"{user_name} you're a little child")
elif (user_age <= 15):
    print(f"{user_name} you're a young teen")
elif (user_age <= 18):
    print(f"{user_name} you're a grown up teenager")
elif (user_age <= 34):
    print(f"{user_name}you're a young adult")
elif (user_age <= 64):
    print(f"{user_name} you're a grown up adult")
elif (user_age <= 100):
    print(f"{user_name} you're a Older Adulthood")
def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")


user_profile = {
    "id": 101,
    "first_name": "Miguel",
    "last_name": "Mario",
    "age": 40,
    "country": "United States",
    "state": "Colorado",
    "occupation": "Developer",
    "language": "Python",
    "level": "Junior",
    "is_active": True,
    "program": "Backend Bootcamp",
    "editor": "VS Code",
    "terminal": "PowerShell",
    "operating_system": "Windows",
    "version_control": "Git",
    "platform": "GitHub",
    "topic": "Algorithms",
    "project": "Data Structures"
}
print_all_pairs(user_profile)


#* What is the time complexity?

# The time complexity is O(n²); even though we are only passing 
# a dictionary, we iterate over it twice using "FOR LOOPS", 
# making the execution time proportional to the square of 
# the number of dictionary keys.


#* How long does it take if there are 1 million keys?

# For n = 1,000,000 keys, given an O(n²) complexity, the program 
# will perform 1,000,000 × 1,000,000 = 1,000,000,000,000 (one trillion) 
# iterations/print operations.
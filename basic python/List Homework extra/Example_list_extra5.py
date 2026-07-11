my_list = []
new_list = []

for index in range(0, 5):
    word = input(f"Enter 5 words for your list:")
    my_list.append(word)
    if (len(word) > 4):
        new_list.append(word)

print()
print(new_list)
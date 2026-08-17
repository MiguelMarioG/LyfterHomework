# Search type 1
def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False


# Search type 2
def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


target1 = 50
example_list = [
    64, 34, 25, 12, 22, 11, 90, 45, 78, 23,
    89, 15, 67, 33, 50, 8, 95, 14, 52, 71,
    3, 41, 88, 29, 60, 17, 82, 36, 5, 99,
]

target2 = 8
another_example_list = [
    42, 18, 95, 7, 63, 21, 84, 50, 11, 76,
    39, 2, 88, 31, 57, 14, 69, 93, 25, 48,
    8, 71, 35, 82, 19, 60, 4, 97, 26, 53,
    12, 79, 44, 1, 66, 38, 85, 23, 90, 15,
]

target3 = 20
ordered_example_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]

result1 = linear_search(example_list, target1)
print(result1)
result2 = binary_search(another_example_list, target2)
print(result2)
result3 = binary_search(ordered_example_list, target3)
print(result3)


#* What is the complexity of each algorithm?

# In the first search, the time complexity is O(n) because we are 
# processing a list of "n" elements by iterating through it
# —from start to finish— until the target value is found. 
# The space complexity is O(1) because we are simply searching 
# for a specific value within a given list and a single target variable.

# In the second search, the time complexity is O(log n) because, 
# while we also receive a list, we iterate using an elimination strategy
# —discarding halves based on whether the value is lower or higher than 
# the target— which requires the list to be sorted in order to work. 
# The space complexity is O(1) because, although we create variables like 
# "low," "mid," and "high," they do not require storage proportional 
# to the list; whether the list has 1 element or 100,000,000, there 
# is no additional space usage associated with those variables.


#* Under what conditions is it best to use each one?

# The first search method is suitable when the list is small and you are 
# certain that for some reason, you cannot or should not sort the list
# —a step that is essential for binary search—; however, it can be 
# slower if the list is very large.

# The second search method can be used regardless of whether the list 
# is small or huge, as it employs a logical search approach that reduces 
# time and makes the process more efficient than a linear search. 
# Note, however, that sorting the list beforehand is mandatory in order to
# make it work the search.


#* What happens if the list is not sorted?

# The first search works without any issues, as it searches the list 
# regardless of the order.

# For the second search, however, it is absolutely mandatory for the 
# list to be sorted; the search logic requires this, and it would 
# not work otherwise.
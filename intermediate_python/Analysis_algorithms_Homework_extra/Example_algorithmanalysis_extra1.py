# Version 1
def manual_add(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result


# Version 2
def add_formula(number):
    return number * (number+1)//2


num = 8

result_one = manual_add(num)
print("Version #1", result_one)
result_two = add_formula(num)
print("Version #2", result_two)


#* What is the complexity of each version?

# In version #1, the time complexity is O(n) because, 
# although we are simply passing a variable "number" 
# with a specific value, the complexity increases due 
# to the "FOR LOOP" using a range; iterating through 
# the variable's full value takes a long time. Furthermore, 
# the line "result += i" effectively results in the 
# operation running "n times" based on that value.

# In version two, the time complexity is O(1). We pass 
# the same "number" value, but the function performs 
# a mathematical operation that yields the result directly. 
# This eliminates the need for a "FOR LOOP" to iterate 
# through every value up to the total, thereby reducing 
# the time required to obtain the result.

# Regarding space complexity, both versions are O(1) 
# because we are simply receiving a single value;
# we are not copying or adding to it, but merely reading it.


#* Which version would you use if number = 1,000,000,000? Why?

# I would use version 2 because, even if the value were 
# in the trillions, I would never need to iterate over 
# the value of each element using a "FOR LOOP" to obtain 
# the result—as is required in version 1—since version 2 
# simplifies the process using a mathematical operation.
grade_quantity = int(input("Enter the total number of grades "))
var = 1
grade_approved = 0
average_grade_approved = 0
grade_disapproved = 0
average_grade_disapproved = 0
grade_total = 0
average_grade_total = 0
grade = 0

print()

while (var <= grade_quantity):
    grade = int(input(f"Enter your Grade {var}: "))
    if (grade >= 70):
        grade_approved += 1
        average_grade_approved += grade
    else:
        grade_disapproved += 1
        average_grade_disapproved += grade
    grade_total += grade 
    var += 1

print() 

if(grade_approved == 0):
    print("You dont have any grade approved")
    print()
else:
    average_grade_approved = average_grade_approved // grade_approved
    print(f"The quantity of the approved grades is: {grade_approved}")
    print(f"The average of the approved grades is: {average_grade_approved}")
    print()

if(grade_disapproved == 0):
    print("You dont have any Grade disapproved")
    print()
else:
    average_grade_disapproved = average_grade_disapproved // grade_disapproved
    print(f"The quantity of the disapproved grades is: {grade_disapproved}")
    print(f"The average of the disapproved grades is: {average_grade_disapproved}")
    print()

average_grade_total = grade_total // grade_quantity
print(f"The average of the grade total is: {average_grade_total}")

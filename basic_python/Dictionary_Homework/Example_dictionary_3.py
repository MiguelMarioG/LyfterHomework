list_of_keys = ["access_level", "age"]
list_employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}


for index in list_of_keys:
    list_employee.pop(index)

print (list_employee)
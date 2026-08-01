def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"Argument {arg} is not a number!")
        
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"Argument {key}={value} is not a number!")
        
        return func(*args, **kwargs)
    return wrapper


@validate_numbers
def add_numbers(a, b):
    return a + b


print(add_numbers(10, 5))
print(add_numbers(10, "hello"))
print(add_numbers(9, value = "Robot"))


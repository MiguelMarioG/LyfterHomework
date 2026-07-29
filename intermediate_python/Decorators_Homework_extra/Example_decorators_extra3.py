from datetime import datetime
from functools import wraps


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, bool) or not isinstance(arg, (int, float)):
                raise TypeError(f"The Argument '{arg}' is not numeric")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(map(str, args))
        now = datetime.now()
        print(f"func:{func.__name__} - args: {args_str} - [{now}] - Result: {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a: float, b: float):
    return a * b


result = multiply(3, 4)
print(f"Result: {result}")
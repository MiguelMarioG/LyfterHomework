def mathematical_function(func):
    def wrapper(a, b):
        print(f"Arguments: {a}, {b}\n")

        result = func(a, b)
        
        print(f"Result: {result}")
        return result
    return wrapper

@mathematical_function
def multiply(a, b):
    return a * b

multiply(3, 4)


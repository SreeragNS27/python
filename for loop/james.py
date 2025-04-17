def uppercase_decorator(func):
    def wrapper():
        print("2")
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        print("1")
        result = func()
        return f"{result}!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello"

print(greet())
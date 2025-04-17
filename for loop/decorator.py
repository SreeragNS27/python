# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()  

# Decorating Functions with Parameters

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,5)
# divide(2,0)

# Chaining Decorators in Python
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner /


# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner


# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")
# import pickle
# pickle_off = open ("datafile.txt", "rb")
# emp = pickle.load(pickle_off)
# print(emp)
# import pickle
# EmpID = {1:"sreerag",2:"53050",3:"IT",4:"38",5:"Flipkart"}
# pickling_on = open("EmpID.pickle","wb")
# pickle.dump(EmpID, pickling_on)
# pickling_on.close()

# import pickle
# pickle_off = open("EmpID.pickle", 'rb')
# EmpID = pickle.load(pickle_off)
# print(EmpID)
# import math
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# d = b**2 - 4*a*c

# if d > 0:
#     root1 = (-b + math.sqrt(d)) / (2*a)
#     root2 = (-b - math.sqrt(d)) / (2*a)
#     print("root1 : "+str(root1) ,"\nroot2 : "+str(root2))
# elif d == 0:
#     root = -b / (2*a)
#     print(" Root is:",root)
# else:
#     print("No real roots")





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

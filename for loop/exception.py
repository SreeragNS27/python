# amount=10000
# if (amount>2999)
# print("you are eligible")

# mark=12000
# a=mark/0
# print(a)

# typeerror

# x=5
# y="hello"
# try:
#     z = x+y
#     print(z)

# except TypeError:
#     print("Error:cannot add an int and a str")

# x=5
# y=0
# try:
#     z=x/y
# except Exception as e:
#     print(e)

# a=[1,2,3]
# try:
#     print("second element :",a[1])
#     print("fourth element : ",a[3])
# except:
#     print("An error occurred")


# def fun(a):
#     if a<4:
#         b=a/(a-3)
#     print("value of b :",b)
# try:
#     fun(3)
# except ZeroDivisionError:
#     print("zerodivisionerror occurred  and handled")
# except NameError:
#     print("Nameerror occurred and handled ")

# def abc(a,b):
#     try:
#         c=((a+b)/(a-b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print(c)

# abc(2,3)
# abc(3,3)

# try:
#     k=5//0
#     print(k)
# except ZeroDivisionError:
#     print("can't divide by zero  ")
# finally:
#     print("this always executed ")

# try:
#     raise NameError("hi there")
# except NameError:
#     print("an exception")
#     raise
a=["james","sree","rag","amal"]
# b=[]
# for i in a:
#     if "a" in i:
#         b.append(i)
# print(b)
b=[i for i in a if "a" in i]
print(b)

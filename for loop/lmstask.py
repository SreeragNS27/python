# a=int(input('enter a number :'))
# b=0
# c=1
# while a>0:
#     d=a%10
#     b=b+d
#     c=c*d
#     a//=10
# if b==c:
#     print("it is a spy number ")
# else:
#     print("not spy number")

# strong number
# import math
# a=int(input("enter a number "))
# f=a
# b=0
# c=0
# while f>0:
#     c=f%10
#     b=b+math.factorial(c)
#     f//=10
# if b==a:
#     print("it is a strong number ")
# else:
#     print(" not strong number ")

# prime number 

# a=int(input("enter a number : "))
# b=0
# for i in range(2,a):
#     if a%i==0:
#         print("its not prime")
#         break
# else:
#         print("it is prime number ")

# palindrome 


# a=int(input("enter a number : "))
# x=a
# f=len(str(a))
# b=0
# c=0
# for i in range (0,f):
#     c=a%10
#     b=b*10+c
#     a//=10
# if b==x:
#     print(str(b),"is a palindrome")
# else:
#     print(str(b),"is not palindro")

# factors of a given number

# a=int(input("enter the number : "))
# for i in range (1,a+1):
#     if a%i==0:
#         print(i)

# multiplication table

a=int(input("enter a number : "))
for i in range(1,11):
    b=a*i
    print(a,"*",i,"=",b)
#1. with argument,with return type
# 2.without argument,with return type
# 3.with argument,without return type
# 4.without argument,without return type

# without argument,without return type
# def baba():
#     a=10
#     b=23
#     c=b-a
#     print(c)
# baba()

# with argument,without return
# def sef(a,b):
#     c=a+b
#     print(c)
# a=10
# b=30
# sef(a,b)


# without argument,with return
# def sample():
#     a=10
#     b=30
#     return a+b
# c=sample()
# print(c)

# with argument,with return

# def let(a,b):
#     return a+b
# d=12
# f=34
# c=let(d,f)
# print(c)

# find the square

# def sample():
#     a=4
#     return a**2
# c=sample()
# print(c)

# even or odd

# def let(a):
    
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# let(7)

# larger number

# def sample(a,b):
#     if a>b:
#         return a
#     elif b>a:
    
#       return b
# a=18
# b=12
# c=sample(a,b)
# print(c)

# factorial of a number

# def fac(a): 
#     b=1  
#     for i in range(1,a+1):
#         b=b*i
#     return b
# a=5
# c=fac(a)
# print(c)

# reverse the string

# def rev(a):
#     b= a[::-1]
#     return b
# a="hello"
# c=rev(a)
# print(c)

# count numbers of vowels

# def vowel(a):
#     b=0
#     c="a","e","i","o","u"

#     for i in a:
#         if i in c:
#             b+=1
#     return b
# a="apapleeo"
# d=vowel(a)
# print(d)

# def prime(a):
#     b=0
#     e="prime"
#     f="not"
#     for i in range(1,a+1):
#         if a%i==0:
#             b+=1
#     if b<=2:
#         return e
#     else:
#         return f
# c=prime(a=13)
# print(c)

# 

# def fib(a):
#     b=0
#     c=1
#     d=0
#     f=[]
#     f=[b,c]
#     for i in range(a-2):
#         d=b+c
#         b=c
#         c=d
#         f.append(d)
#     print(f)
# a=5
# fib(a)
# a=input("enter the value")
# b=[]
# for  i in a:
#     if a.count(i)==1:
#             b+=i
# print(b[0])
# def add(c):
#     if c=="1":
#         d=a+b
#         return d
# def sub(c):
#     if c=="2":
#         m=a-b
#         return m
# def multi(c):
#     if c=="3":
#         f=a*b
#         return f
# def div(c):
#     if c=="4":
#         g=a/b
#         return g
    

# while True:
#     print("choose you option""\n1.add""\n2.sub""\n3.mulit"
#     "\n4.div" )
    
#     c=input("choose your operator")
#     if c=="1":
#         a=int(input("enetr the number : "))
#         b=int(input("enter the number : "))
#         f=add(c)
#         print(f)
        
#     elif c=="2":
#         a=int(input("enetr the number : "))
#         b=int(input("enter the number : "))
#         z=sub(c) 
#         print(z)
        
#     elif c=="3":
#         a=int(input("enetr the number : "))
#         b=int(input("enter the number : "))
#         y=multi(c)
#         print(y)
        
#     elif c=="4":
#         a=int(input("enetr the number : "))
#         b=int(input("enter the number : "))
#         x=div(c)
#         print(x,"is the numb er")
#     break

    # bank account
account={}
def create():
    ac={}
    PH=int(input("enter the number : "))

    if len(str(PH))==10:
        NA=input("enter your name : ")
        AM=int(input("enter the amount :"))
        if PH  not in account:
            ac["name"]=NA
            ac["phone"]=PH
            ac["amount"]=AM  
            account[PH]=ac   
        else:
            print("already have account in this number ") 
            
    else:
        print("no 10 digits in phone number")
        return create()
        
def update():
    ac={}
    
    PH=int(input("enter the number : "))
    if PH in account:
        NA=input("enter your name : ")
        AM=int(input("enter the amount :"))
        ac["name"]=NA
        ac["amount"]=AM
        account[PH]=ac
    else:
        print("not found")
def delete():
        
        PH=int(input("enter the number : "))
        if PH in account:
            del account[PH]
            print(account)
def deposit():
    
    PH=int(input("enter the number : "))
    if PH in account:
        ac={}
        DE=int(input("enter the amount"))
        c=account[PH]["amount"]
        total=c+DE
        ac["amount"]=total
        account[PH]=ac
        print(ac)
    else:
        print("not matching")
def withdraw():
    
    PH=int(input("enter the number : "))
    if len(str(PH))==10:
        if PH in account:
            ac={}
            DE=int(input("enter the amount"))
            if DE<=account[PH]["amount"]:

                c=account[PH]["amount"]
                balance=c-DE
                ac["amount"]=balance

                account[PH]=ac
                print(ac)
                print("withdraw successfully completed")
            else:
                print("insufficient fund")
        else:
            print("not matching")
    else:
         
        print("no 10 digits in phone number")
        return withdraw()

        
        


    
while True:
    print("1.create""\n2.update""\n3.delete""\n4.deposit""\n5.withdraw")
    a=input("choose your option")
    if a=="1":
      f=  create()
      print("successfully created ")
    elif a=="2":
        f=update()
        print("successfully updated " )
    elif a=="3":
        f=delete()
        print("successfully deleted ")
    elif a=="4":
        f=deposit()
        print("successfully deposit")
    elif a=="5":
        f=withdraw()
        

    




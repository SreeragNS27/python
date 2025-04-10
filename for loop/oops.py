# class Employee:
#     id=10
#     name="sreerag"
#     def display(sam):
#         print(sam.id,sam.name)


# obj=Employee()
# del obj.id
# obj.display()

# sample=Employee()
# sample.display()

# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# a=input("enter your modelname :")
# b=int(input("enter the year :"))
# c1=car(a,b)
# c1.display()

# c2=car("tesla",2020)
# c2.display()
# class cal:
#     def __init__(self):
#         print("calculating")
#     def add(self,a,b):
#         print(" the answer is :", a+b)
#     def sub(self,a,b):
#         print("the answer is : ",a-b)
#     def div(self,a,b):
#         print("the answer is : ",a/b)
#     def multi(self,a,b):
#         print("the answer is : ",a*b)
    
# while True:

#     print("1.add","\n2.sub","\n3.div","\n4.mult")
#     c=input("choose your option")

#     if c=="1":
#         a=int(input("enter a value : "))
#         b=int(input("enter the 2nd value :"))
#         c1=cal()
#         c1.add(a,b)
#     elif c=="2":
#         a=int(input("enter a value : "))
#         b=int(input("enter the 2nd value :"))
#         c1=cal(a,b)
#         c1.sub()
#     elif c=="3":
#         a=int(input("enter a value : "))
#         b=int(input("enter the 2nd value :"))
#         c1=cal(a,b)
#         c1.div()
#     elif c=="3":
#         a=int(input("enter a value : "))
#         b=int(input("enter the 2nd value :"))
#         c1=cal(a,b)
#         c1.multi()
#     else:
#         print("wrong selection")
#         continue


# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("john",101,22)
# print(getattr(s,'name'))
# setattr(s,"age",23)
# print(getattr(s,'age'))
# print(hasattr(s,'id'))
# delattr(s,'age')
# print(s.age)




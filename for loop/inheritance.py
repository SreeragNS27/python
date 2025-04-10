# class Animal:
#     def speak(self):
#         print("animal speaking ")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()

# multi level inheritance

# class Animal:
#     def speak(self):
#         print("animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# class Dogchild(Dog):
#     def eat(self):
#         print("eating bread")
# d=Dogchild()
# d.eat()
# d.bark()
# d.speak()

# multiple inheritance


# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.summation(10,20))
# print(d.multiplication(10,20))
# print(d.divide(10,20))

# Hierarchical inheritance

# class Parent:
#     def fun1(self):
#         print("this function is in parent class")
# class Child1(Parent):
#     def fun2(self):
#         print("this function is in child 1")
# class Child2(Parent):
#     def fun3(self):
#         print("this function is in child 2")
# obj1=Child1()
# obj2=Child2()
# obj1.fun1()
# obj1.fun2()
# obj2.fun3()
# obj2.fun1()

# class Person:
#     def display_person(self):
#         print("name :",name,"\nage: ",age)
    
# class Student(Person):
#     def __init__(self,student_id,grade):
#         self.student_id= student_id
#         self.grade= grade
#     def display_student(self):
        
#         print("student id : ",self.student_id)
#         print("grade : ",self.grade)
# name=input("enter your name : ")
# age=int(input("enter your age : "))
# student_id=int(input("enter your id : "))
# grade=input("enter the grade : ")

# stud=Student(student_id,grade)
# stud.display_student()
# stud.display_person() 




    

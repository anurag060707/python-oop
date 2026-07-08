#a Python program to create a class with attributes name and age. 
class Student:
    def __init__(self,fullname,age):
        self.name=fullname
        self.age=age
fullname=input("enter name:")
age=int(input("enter age:"))        
s1=Student(fullname,age)
s1.name
s1.age
print(s1.name)
print(s1.age)        
        

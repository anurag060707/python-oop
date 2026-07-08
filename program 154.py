#a Python program to access class attributes using an object. 
class Student:
    name="anurag sharma"
    age=20
s1=Student()
s1.name
s1.age
print(s1.name)
print(s1.age) 

#method 2
class student2:
    pass
s1=student2()
s1.name=input("enter name:")
s1.age=int(input("enter age:")) 
print(s1.name)
print(s1.age)  
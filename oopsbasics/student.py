# Defining and using static fields 

class Student:
    major = "CSE"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

s1 = Student(1, "John")
s2 = Student(3, "Bill")
print(s1.major) # Static field
print(s2.major) # Static field
print(s1.name)
print(s2.name)

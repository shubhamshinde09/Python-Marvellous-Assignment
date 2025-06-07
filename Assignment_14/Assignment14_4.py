# 4 Student with class variable
class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")


s1 = Student("Amit", 1)
s1.display()
Student.school_name = "XYZ School"
s1.display()
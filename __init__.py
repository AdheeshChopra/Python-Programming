# init or constructor

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database...")


s1 = Student("Adheesh", 97)
print(s1.name, s1.marks)

s2 = Student("Chopra Saab", 99)
print(s2.name, s2.marks)
class Student:
    college = "MIET"
    # name = "anonymous"      # class attribute

    def __init__(self, name, marks):
        self.name = name        # object attribute > class attribute
        self.marks = marks
        print("Adding new student in database...")


s1 = Student("Adheesh", 97)
print(s1.name)

s2 = Student("Chopra Saab", 99)
print(s2.name, s2.marks)

print(Student.college)
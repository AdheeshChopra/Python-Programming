class Student:
    college = "MIET"

    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks
    
    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("Adheesh", 97)
s1.welcome()
print(s1.get_marks())


# Question 1

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "\nYour average score is:", sum/3)


s1 = Student("Adheesh Chopra", [97, 98, 99])
s1.avg()

s1.name = "Chopra Saab"
s1.avg()
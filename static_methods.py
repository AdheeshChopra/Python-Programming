class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod       # decorator
    def hello():
        print("Hello")
    
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "\nYour average score is:", sum/3)


s1 = Student("Adheesh Chopra", [97, 98, 99])
s1.avg()
s1.hello()
# Question 1

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# Question 2

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "500000")

engg1 = Engineer("Adheesh Chopra", 19)
engg1.showDetails()


# Question 3

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 20)
ord2 = Order("Tea", 15)

print(ord1 > ord2)
# SINGLE INHERITANCE

class Car:

    color = "Black"

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")

print(car1.name)
print(car1.start())
print(car1.color)


# MULTILEVEL INHERITANCE

class Car:

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesal")
car1.start()


# MULTIPLE INHERITANCE

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


# SUPER METHOD

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = ToyotaCar("prius", "electric")
print(car1.type)
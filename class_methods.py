class Person:
    name = "Anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Adheesh"
        # Person.name = name
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Adheesh Chopra")
print(p1.name)
print(Person.name)
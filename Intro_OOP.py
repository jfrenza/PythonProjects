#Introduction to Object Oriented Programming

class Dog:
    # Methods are functions that are created inside a class

    # The __init__ method is a Dunder Method. This allows us to instantiate
    # an object right when it is created; therefore the
    # __init__ method will be called every time we instantiate a new object
    def __init__(self, name, age):
        self.name = name # Here we've created an atrribute of the class Dog
        self.age = age

    def bark(self):
        print('bark')

    def get_age(self):
        return self.age


# The variable d is assing to an instance of the class Dog (Instantiating)
d = Dog('Felipe', 5)
d.bark() # I can call the bark method to my object d
print(d.get_age())

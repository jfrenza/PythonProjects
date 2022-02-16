# Inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I am {self.age} years old")

class Cat(Animal):
    def speak(self):
        print('Meow')

class Dog(Animal):
    def speak(self):
        print('Bark')

Pet = Animal('Motas', 10)
Pet2 = Dog('Tango', 8)
Pet3 = Cat('Sombra', 10)

Pet2.speak()
Pet3.speak()

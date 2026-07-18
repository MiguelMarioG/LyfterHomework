class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Make a Sound"

class Dog(Animal):
    def speak(self):
        return "Wouf, Guau"

class Cat(Animal):
    def speak(self):
        return "Pssst, Miau"

specie = Animal("Fepo")
dog = Dog("firulais")
cat = Cat("Miaut")

print(dog.speak())
print(cat.speak())
print(specie.speak())

print(f"The Dog name is: {dog.name}")
print(f"The Cat name is: {cat.name}")
print(f"The Animal name is: {specie.name}")
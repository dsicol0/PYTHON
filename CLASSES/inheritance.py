class Animal:
        def __init__(self, name):
            self.name = name
            self.isAlive = True
        
        def eat(self):
            print(f"{self.name} is eating")

        def sleep(self):
           print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Axel")
cat = Cat("Garfield")
mouse = Mouse("Ratatouille")

print(dog.name)
mouse.eat()
mouse.sleep()
print(cat.name)
print(cat.isAlive)
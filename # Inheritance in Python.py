# Inheritance in Python 
'''
Inheritance: Child class inherit the all properties of parent class 
    it promotes code reusability, Extensibility, Maintainability, Polymorphism support

'''
class Animal:
    def sound(self):
        return " Producing sound"
class Dog(Animal):
    def sound(self):
        return "bark"
    
d = Animal()
d = Dog()

print(d.sound())
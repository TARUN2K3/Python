# Abstraction in Python
'''
Abstraction : Hiding the internal details only showing essential features.
    implementaion using Abstract base class module(abc)
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
    def start(self):
        return "car is start"
class Bike(Vehicle):
    def start(self):
        return "Bike is start"
    
v1 = car()
v2 = Bike()
print(v1.start())
print(v2.start())
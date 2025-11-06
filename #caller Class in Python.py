#caller Class in Python
'''Caller class” usually refers to the class or object that calls (or invokes) a method or function from another class in Python'''
class Callee:
    def greet(self):
        print("Hello from Callee class!")


class Caller:
    def call_greet(self):
        # Creating an object of Callee class
        c = Callee()
        # Calling a method of Callee class
        c.greet()
        print("Greeting called from Caller class.")


# Creating object of Caller class
obj = Caller()
obj.call_greet()
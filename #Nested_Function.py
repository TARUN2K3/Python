#Nested_FUnction
'''Nested function means calling function define inside another function'''
#Simple_Nested_Function
def outer():
    print("Hello form outer Function")
    def inner():
        print("Hello from inside Function")
    inner()
outer()

#Returnning the Innner Function

def outer():
    def inner():
        print("Hello form inner function")
    return inner
greet = outer()
greet()

#Nested Function with Parameter
def outer(name):
    def inner():
        print(f"Hello, {name}!")  # Accessing outer function variable
    inner()

outer("Tarun")

#-----------------------------------------------------
def calculator(a, b):
    def add():
        return a + b

    def multiply():
        return a * b

    print("Sum:", add())
    print("Product:", multiply())

calculator(4, 5)

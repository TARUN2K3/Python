#Function_as_Object
'''In python function is the instance of function class and can be assign to be variable.'''

def greet(name):
    return f"Hello {name}"

say_hello = greet

print(greet("Tarun"))
print(say_hello("Tarun"))
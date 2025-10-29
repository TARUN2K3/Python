#Decorator in Python
'''Decorator in the python is the function that modify the behaviour of the another function means add extra functionality'''
#Synatx
'''@decorator_name
def function_name():
    body
    
Similar like :- function_name = decorator_name(function_name)
'''
def greet_message(func):
    def wrapper():
        print("Hello before Decorator")
        func()
        print("Hello after Decorator")
    return wrapper

@greet_message
def hello_message():
    print("hello_message")

hello_message()

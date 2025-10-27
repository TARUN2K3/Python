#Closure_Function
'''A closure is an inner function that “remembers” variables from the outer function even after the outer function is done'''
def outer_function(message):
    def inner_function():
        print("Message:", message)
    return inner_function

# Create a closure
my_closure = outer_function("Hello, Tarun!")

my_closure()

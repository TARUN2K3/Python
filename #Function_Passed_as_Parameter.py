#Funcction_Passed_as_Parameter
def greet(name):
    return f"Hello, {name}!"

def display_message(func):
    message = func("Tarun")   # calling the function passed as parameter
    print(message)

display_message(greet)

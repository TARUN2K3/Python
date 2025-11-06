#Function Arguments in Python
'''when we define function it can accept input it is called Parameter
    when we call function we can pass actual value it is called Argument'''

#There are different ways to pass argument:--
#Postional argument :- They are matched by Position of parameter in which order they are passed.
#Keyword argument :- we explicitly specify which parameter each value belongs to.
#Mixed Argument :- we Combine Both Type arguments (Positional and Keyword) in which postional comes first.

#Rules:
#Positional Argument always call first before keyword argument.


#---------------------------------------------------------------------------
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

# Calling the function using positional arguments
student_info("Tarun", 21, "Python")
#----------------------------------------------------------------------------
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

# Calling using keyword arguments
student_info(age=21, name="Tarun", course="Python")
#----------------------------------------------------------------------------
def order(item, quantity, price):
    print(f"Item: {item}, Quantity: {quantity}, Price: {price}")

# Mixed arguments
order("Laptop", quantity=2, price=75000)


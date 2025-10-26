#Modules in Python
#A module in Python is simply a file containing Python code — it can include functions, classes, and variables that can be imported and reused in other Python programs.
'''module is a Python file (.py) that contains definitions and statements.
You can import it into another program to use its contents.'''

#Built In------------------------------------------------------------------
import math as m
print(m.factorial(5))  # 120

#User Define---------------------------------------------------------------
import math_utils

print(math_utils.add(5, 3))       # Output: 8
print(math_utils.subtract(5, 3))  # Output: 2
#--------------------------------------------------------------------------
def greet():
    print("Hello from the module!")

if __name__ == "__main__":#This is used to check whether a Python file is run directly or imported as a module.
    print("This code runs only when executed directly.")
else:
    print("This code runs when imported.")


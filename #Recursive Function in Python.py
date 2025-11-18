#Recursive Function in Python
''' Recursive function in python is the function calling itself it include recursive call and base condition 
    Recursive call :- the function call itself with modified argument
    base condition :- vital stopping condition prevent infinite recursion
    Uses :-	Factorial, Fibonacci, DFS, nested structures
    Limitation :-	Recursion depth, memory usage
    Recursive function are alternative to loops
'''
#5! = 5 × 4 × 3 × 2 × 1
#0! = 1


def factorial(n):
    if n == 0:       # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call
print(factorial(5))

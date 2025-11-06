#What_are_function_in_python?
'''Function is block of code which perform specific task it help to make program modular, reusable and easily maintainable.'''
'''Take parameter as input and output as result'''

#Synatx:-

def function_name(parameter):
    '''function body'''
    return result

#Simple Function

def greet(name): #Function define
    print(f"hii,{name}") ##Function print

greet("Tarun") #Function calling

#Function with Return Value
def add(a,b):
    return a+b
result = add(10,20)
print("addition :",result)

#Function with default parameter

def add(a=10,b=30):
    return a+b
result = add()
print("addition :",result)

#Function with Multiple Return value

def multiple_opertaion(a,b):
    return a+b, a-b, a*b
addition, substraction, multiplication = multiple_opertaion(4,1)
print(addition, substraction, multiplication)


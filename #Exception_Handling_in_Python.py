#Exception Handling in Python
'''
Exception handling in Python is a Mechanism to Handle Run time Error like - Division by Zero, Index error, value error,
 File not found, type error, Key error, Name error

 1.Zero Division Error : Diving a Number by Zero
 2.FileNotFoundError: File not found in the disk
 3.Index error : Index out of the range in list or string
 4.Type error: Operation on Incompatible Datatype
 5.Value Error: Invalid value(e.g. Converting str to Int)
 6.Key Error: Accessing Missign Dictionary key from the Dictionary
 7.Name Error : variable Not define

Handling These error we use:
1.try : contains Code that may raise an error
2.except : handle specific exception
3.else : runs is not Exception Occur
4.finally: always execute

'''
try:
    a = int(input("Enter No. a: ")) 
    b = int(input("Enter No. b: "))
    c = a//b
except(ZeroDivisionError) as e:
    print(e)
except(ValueError) as e: 
    print(e)
else:
    print(c)
finally:
    print("code run finally statement")

# Multiple Exception in One Block
try:
    x = int('abc')
except(ValueError, TypeError) as e:
    print(e)

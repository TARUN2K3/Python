#Built-in function for object and attribute
#type() --> print the type of variable in python
print(type(10))
print(type(10.0))
print(type("tarun"))
print(type([74921,290]))
print(type((8503,5093)))
print(type({3,4,5,7}))
print(type({'a':1}))
print(type(None))
print('---------------------------')
#isinstance() --> return the instance of certain class in boolean
x = 10
print(isinstance(x,int))
print(isinstance(x,float))
print('---------------------------')
#hasattr() --> return attribute has cetrain method in boolean
x = 'hello'
print(hasattr(x, 'lower'))
print(hasattr(x, 'search'))
print(hasattr(x, 'find'))
print('---------------------------')
#getattr --> retrive attribute and function form module then call its function
import math
print(getattr(math, 'pi'))
square_root_func = getattr(math, 'sqrt')
print(square_root_func(25))
print('---------------------------')
#id() --> it gives the id of the attribute
x = 10
y = 10
print(id(x))
print(id(y))
l1 = [12,3,44,4]
l2 = [12,3,44,4]
print(id(l1))
print(id(l2))
print('---------------------------')
# dir() --> this gives all method and attribute of the module
print(dir([1,23,4]))
print(dir(math))
print(dir({'a':1}))
print('---------------------------')
# repr() --> this print with single quotation mark('')
print(repr("tarun"))
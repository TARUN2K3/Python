#Local and Global variable in Python
''' Local variable are those variable which are define inside the function and accesible only within that function
    Global variable are those variable which are define outside the function and accesible anywhere in the program
'''

#Local variable inside the function
def fun():
    l = 10
    print(l)

fun()

#Global variable accessed inside the function
g = 10
def global_fun():
        a = 9
        print("global:",g)
        print("local:",a)

global_fun()
print(g)

#Attempting modifying global varibale inside the function without global keyword
g = 10
def global_fun():
        a = 9
        g = 199
        print("global(local g):",g)
        print("local:",a)

global_fun()
print(g)

#Modifying global variable inside the function with global variable
g = 10
def global_fun():
        global g
        a = 9
        g = 199
        print("global(local g):",g)
        print("local:",a)

global_fun()
print(g)

#using local() and global() keywords

x,y,z =1, 2, 3

def varibale():
       a, b, c = 5,6,7
       print(locals())
       print(globals())
varibale()

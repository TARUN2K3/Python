#variable_length_positional_argument
'''Python allows us to pass any number of positional argument using *args keyword 
    variable length positional argument packed in the form of "tuplre" in the function
    parameter inside the function before *args must be positional argument
    parameter inside the function after *args must be keywords arugument'''

def function(*args):
    print(args)

function(12,2,3,3,3,4)

def function1(a, b, *args):
    print(args, a, b)

function1(1,2,3,3)

def function2(a,b,*xyz,c,d):
    print(a,b,xyz,c,d)
 
function2(1,2,[9,8,7],c=1,d=2)


def function3(a,b,*xyz,c,d):
    print(a,b,xyz,c,d)

# function3(c=1,d=2[9,8,7],1,2) #This will show error





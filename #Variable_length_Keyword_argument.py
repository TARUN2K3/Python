#Variable_length_Keyword_argument
''' **kwargs (short for keyword arguments) allows a function to accept any number of keyword arguments, arguments passed as key value pairs
    resulting the dictionary of key value pair
    iterating over `kwargs.items()` allows access to individual key-value pairs for processing

    Parameter before **Kwargs is can be positional or keywords argument
    paramter between *args and **kwargs must be keyword only.
    if parameter after **kwargs is syntax error.
'''     

def function(**kwargs):
    print(kwargs)

function(a=12,b=22,c=32)

def function0(**keywords):
    print(keywords)

function0(a=1,b=2,c=3)


def function1(a,**kwargs):
    print(a,kwargs)

function1(1,b=2,c=3)

def function2(*args,a,**kwargs):
    print(args,a,kwargs)

function2(2,1,a=1,b=2,c=3)


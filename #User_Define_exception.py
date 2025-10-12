#User_Define_exception
'''Here is the Example of user efine Exception where Negative Number Error'''

class NegativenumberError(Exception):
    """This is the Negative Number"""
    pass

def CheckNumber(n):
    if n<0:
        raise NegativenumberError("Negative no. are not allowed")
    else:
        print(f'Number {n} is vaild')

try:
    CheckNumber(-1)
except NegativenumberError as e:
    print(e)
except ValueError as e:
    print(e)

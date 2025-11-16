#Generator in python
'''generator is the special kind of iterator that is created using a function with yield, producing values lazily (on demand)
    yield pause the function state and return the value unlike `return` which teminate the function
'''
def days():
    days = ['sun', 'mon', 'tue', 'wed', 'thrus', 'fri', 'sat']
    i = 0
    while True:
        yield days[i]
        i = (i+1)%7

days_generator = days()
print(next(days_generator))
print(next(days_generator))
print(next(days_generator))
print(next(days_generator))
print(next(days_generator))
print(next(days_generator))
print(next(days_generator))

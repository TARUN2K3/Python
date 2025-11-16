#Iterator in Python
'''Iterator is the object in python that allows you to traverse element one at a time using next() function
    it remember it current state and start from there when it called 
        iter() is in-bult function takes an iterable and return object
        when iteration reached at end, a StopIteration exception raised and internally handle
        List, tuple, string:- ordered sequence
        set :- unordered
        Dict:- iterating by key element'''

L1 = [1,2,3,4,5,6]
e = iter(L1)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

T1 = (1,2,3,4,5,6)
f = iter(T1)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

S1 = {1,2,3,4,5,6}
t = iter(S1)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
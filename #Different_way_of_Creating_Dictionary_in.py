#Different_way_of_Creating_Dictionary_in_python

#Using Iterable pairs(list or tuple of key value tuple)
'''Passing iterable pair into the `dict()` convert them into dictionary'''
iterable_pair = ([1,"one"],[2,"two"],[3,"three"],[4,"four"])
D1 = dict(iterable_pair)
print(D1)

iterable_pair1 = [[1,"one"],[2,"two"],[3,"three"],[4,"four"]]
D2 = dict(iterable_pair1)
print(D2)

iterable_pair2 = [(1,"one"),(2,"two"),(3,"three"),(4,"four")]
D3 = dict(iterable_pair2)
print(D3)

iterable_pair3 = ((1,"one"),(2,"two"),(3,"three"),(4,"four"))
D4 = dict(iterable_pair3)
print(D4)

# Using zip function
'''`zip()` function take multiple iterable argument and aggeragte element pair like Zip
    This function return zip([1,2],[one,two]) into iterable of (1,"one"),(2,"two")'''

L1 = [1,2,3,4,5,6,7]
L2 = ['one','two','three','four','five','six','seven']
ZD1 = zip(L1,L2)
print(dict(ZD1))

LT1 = (1,2,3,4,5,6,7)
LT2 = ('one','two','three','four','five','six','seven')
LT3 = ('one','two','three','four','five','six','seven')
ZD2 = zip(LT1,LT2)
print(dict(ZD2))


ZD2 = zip(LT1,L2)
print(dict(ZD2))

#Uning Enumerate Function
'''This Function add an index(by default it is ZERO) we can set `start = 1` to each element in an iterable, return tuple (index,element)'''

T1 = ('one','two','three','four','five','six','seven')
E = enumerate(T1)
print(dict(E))

T2 = ['one','two','three','four','five','six','seven']
E = enumerate(T2, start=1)
print(dict(E))
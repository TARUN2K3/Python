#List_Comprehensions

'''It is consise method in python to create new list from iterable by applying expressions and condition within single line of code'''

L1 = [x for x in range(10)]
print(L1)

L2 = [x for x in range(10) if x%2==0]
print(L2)
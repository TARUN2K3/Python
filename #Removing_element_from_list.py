#Removing_element_from_list
'''
1. pop() --> remove element by index, by default it remove last element if index not provided
2. remove() --> it remove element by value it remove only first occurrence
3. clear() --> Remove all element form the list, after clearing it remain define empty list
4. del --> This keyword remove element form the list
'''

L1 = [2,2,4,5,6,77,78]
L1.pop(2)
print(L1)

L1.remove(2)
print(L1)

L1.clear()
print(L1)

L2 = [12,3,4,56,7,8,9]
del L2[3:5]
print(L2)
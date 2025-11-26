#Shallow copy and Deep copy in python

#Shallow copy
'''Copies only the top-level keys and values
Does not create copies of nested objects (inner lists, dicts, etc.)'''
import copy

d1 = {"a": 1, "b": [10, 20]}
d2 = d1.copy()  # shallow copy

d2["b"].append(30)
print(d1)
print(d2)
'''
{'a': 1, 'b': [10, 20, 30]}
{'a': 1, 'b': [10, 20, 30]}
Modifying nested object in d2 affects d1
(because both reference the same list)'''


#Deep copy
'''Creates completely independent copy, including nested objects'''
import copy

d1 = {"a": 1, "b": [10, 20]}
d3 = copy.deepcopy(d1)

d3["b"].append(30)
print(d1)
print(d3)
'''{'a': 1, 'b': [10, 20]}
{'a': 1, 'b': [10, 20, 30]}
Now changes in d3 do not affect d1'''
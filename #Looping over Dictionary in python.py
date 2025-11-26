#Looping over Dictionary in python

#Iterating over dictionary

D1 = {1:"one",2:"Two",3:"Three",4:"Four",5:"Five"}
for i in D1:
    print(i)

for i in D1:
    print(i, D1[i])

#Dictionary method in looping

for i in D1.keys():
    print(i)


for i in D1.values():
    print(i)


for i in D1.items():    #This return tuple like this ex - (1, 'one')
    print(i)

#Accessing Values 1. indexing --> it raise error if key is not exist -->keyerror
#                 2. get(key, default=None)  --> Return value if exist otherwise return none
#                 2. setdefault(key, default=None)  --> if key not exist insert key otherwise Return value if exist otherwise return none

print(D1.get(3))
print(D1.setdefault(4))
print(D1.setdefault(5,'Undefined'))

#Update --> Used to add or modify key–value pairs in a dictionary.
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)
print(d1)

#fromkeys --> Creates a new dictionary with given keys and a single value.

keys = ["name", "age", "city"]
user = dict.fromkeys(keys, "Unknown")
print(user)


#copy --> shallow copy --> Changes in d2 won’t affect d1 unless nested objects are involved
d1 = {"a": 1, "b": 2}
d2 = d1.copy()
print(d2)

#pop --> Removes a specific key and returns its value.
d = {"name": "Tarun", "age": 21}
age = d.pop("age")
print(age)
print(d)

#popitem() -->Remove last inserted item.

d = {"a": 1, "b": 2, "c": 3}
print(d.popitem())
print(d)

#Clear() -->remove all item from Dictonary
d = {"a": 1, "b": 2}
d.clear()
print(d)


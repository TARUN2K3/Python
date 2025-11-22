#Dictionary_in_Python
''' 
    `unordered, mutable collection of key–value pairs`
    Dictionary is the collection of key value pair where each key maps uniquely to value.
    Key must be immutable else value of any type like complex such as list tuple set even other dictionary
    Syntax: {key:value}
    Efficient for searching values by keys'''

#Creating Dictionary

D = {} #this create empty dictionary not set
D1 = {1:"one",2:"two",3:"three",4:"four"}
print(D)
print(D1)

#Adding new element

D1[5] = "Five"
print(D1)

#Accessing not available element
try:
    print(D1[6]) # this shown Key error
except:
    print("error")

#Mixed type of keys and values

D2 = {
    "a" : 3.5,
    "b" : "Tarun",
    "c" : 3+5j,
    "d" : [12,3,3,4,4,5],
    "e" : (12,3,4,"xyz"),
    "f" : {"a":1}
}

print(D2)

#Tarversing element
for key in D2:
    print(f"key:{key},value: {D2[key]}")
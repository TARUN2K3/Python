#Tuple_Comprehension

#Syntax
#T = (*(exp for item in Iterable),) #* use for unpacking otherwise it will create Generator object

#Method 1

T1 = (*(x for x in range(1,5)),)
print(T1)

#Method 2

T2 = tuple(x for x in range(1,5))
print(T2)

#Packing and Unpacking in Tuple
#Tuple Concatenation
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
t3 = t1 + t2
print(t3)

#Tuple repetition
t4 = t1*3
print(t4)

#Packing Multiple Value
t5 = 1,2,3,4,5,6,7,8
print(t5)
type(t5)

#Unpacking
a,b,c,d,e = t1
print(a,b,c,d,e)

a,b,*c = t1
print(a,b,c)

a,*b,c = t1
print(a,b,c)

*a,b,c = t1
print(a,b,c)


a,b,c = t1
print(a,b,c) # This will give error




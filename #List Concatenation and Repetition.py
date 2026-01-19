#List Concatenation and Repetition
 #Concatetion --> '+' and extend()
 #Repetition --> Multipling List by integer
 #Membership Operator --> in or notin
 #List Comparison --> '==', '!=', '<', '>', '<=', '>='

L1 = [1,2,3,4,5,6]
L2 = [8,9,10,11,12,13]
L3 = L1+L2
print(L3)
print(L3+[4])

L1.extend(L2)
print(L1)

L1 = L1*3
print(L1)

print(3 in L1)
print(L1 == L2)
L4 = ['Parun','Sitin','Vinod','Uravshi','red']
L5 = ['Plate','Spoon','chair','cooker','Wifi']

print(L4 > L5)


#Methods in Set

#Adding element in the set

s1 = {'python',1,65,23,68,90,2j+1}
s1.add(43)

print(s1)

#If we try to add the immutable element it will show error

#s1.add([1223,34]) #this throw error

#Removiing element for the set

s1.remove(68)
#If we try to remove element from the set which is not present that will throw error

#s1.remove(101)

s1.pop()
print(s1)
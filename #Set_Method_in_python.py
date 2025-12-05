#Set_Method_in_python
s1 = {1,45,6,90,10,100}
s2 = {"tarun",34,5,7,821,80,100,34,45,1}

s3 = s1 - s2
print(s3)

#s1 -= s2
#print(s1)

u1 = s1 | s2
print(u1)

u2 = s1.union(s2)
print(u2)

i1 = s1 & s2
print(i1)

i2 = s1.intersection(s2)
print(i2)

sd1 = s1 ^ s2
print(sd1)

#s1 ^= s2
#print(s1)

sd2 = s1.symmetric_difference(s2)
print(sd2)
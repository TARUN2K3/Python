#Indexing and Slicing List in Python
'''Indexing is use in python for access or write a single element by position using square bracket list[index]
    Slicing is ude in python for extract or write the sub list by defing the start, stop and step list[start:stop:step]'''

#Read
L1 = [1,2,3,4,5,6,7,8,9]

print(L1[3])
print(L1[-3])
print(L1[:])
print(L1[2:])
print(L1[3:7])
print(L1[-7:-3])
print(L1[7:3])
print(L1[::-1])
print(L1[::2])
print(L1[4:0:-1])
print(L1[-3:-7:-1])

#write

L1[8] = 10
print(L1)
L1[8] = 11
print(L1)
L1[-1] = 0
print(L1)
L1[8:8] = [12]
print(L1)
L1[-1:-1] = [13]
print(L1)
L1[-1:-2] = [14]
print(L1)
L1[-1:-3] = [15]
print(L1)
L1[-1:-10] = [15]
print(L1)
L1[3:0:-1] = [16,17,18]
print(L1)

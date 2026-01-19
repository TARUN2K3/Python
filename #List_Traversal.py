#List_Traversal
'''There are three way to traverse List:
    1. for loop over the element
    2. for loop with range(len(list))
    3. while loop'''

L1 = [4,5,6,7,8,89,0]

for x in L1:
    print(x)

for i in range(len(L1)):
    print(i, L1[i])

i = 0
while (len(L1)>i):
    print(L1[i])
    i = i+1
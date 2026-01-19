#Adding_element_to_the_List_Built-in

'''
1. Append --> append(element) --> add single element at the end of the list
2. extend --> extend(iterable)
3. Insert --> insert(index, element)
4. slicing --> l1[2:2] = [4]
5. copy --> copy()
'''
L1 = [2,3,4,6,7,8,5,0]
L1.append(9)
print(L1)

L2 = [32,4,5,6,7,8,9]
L2.extend([2])
print(L2)

L2.insert(0,1)
print(L2)

L2[1:1] = [55,3]
print(L2)

L3=L2.copy()
print(L3)
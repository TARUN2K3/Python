#Dictionary_Comprehensions_in_Python
'''Dictionary comprehension is compact and expressive way to build dictionaries
    Syntax : use curlt braces `{}`
    general form:{key_expression:value_expression for key, value in iterable}
    '''
#By Iterable pairs

iterable_pair = ([1,"one"],[2,"two"],[3,"three"],[4,"four"])
D1 ={x:y for x,y in iterable_pair}
print(D1)

#By Zip() Function
L1 = [1,2,3,4,5,6,7]
L2 = ['one','two','three','four','five','six','seven']
D2 = {x:y for x,y in zip(L1,L2)}
print(D2)

#By Enumerate() Function

T1 = ('one','two','three','four','five','six','seven')
D3 = {x:y for x,y in enumerate(T1, start=1)}
print(D3)



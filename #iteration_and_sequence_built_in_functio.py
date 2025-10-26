#iteration and sequence built-in function
#sorted(iterable, key=None, reverse=None) --> Return  new sorted List key takes function applied on each element and reverse is true give descending order list
s = [24,248,-2,1,-4,3.0,-10.0]
print(sorted(s))
print(sorted(s,key=abs))
print(sorted(s,key=abs, reverse=True))
print('-----------------------------------------')

#reversed(seq) --> return reverse iterator object do not create new reversed list
rev = reversed(s)
print(rev)
rev = reversed(s)
print(list(rev))
print('-----------------------------------------')

#slice(start=0, stop, step=1) -->  return  silce object indices in sequence
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = a[2:]
print(b)

c = a[:3]
print(c)

# next(it) --> if called again raises stopiteration error\
it = iter(a)
print(next(it))
print(next(it))
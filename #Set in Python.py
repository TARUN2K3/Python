#Set in Python
'''Set is the Unorderd collection of Unique elements, it does not allowed duplicate values and elemnts does not have indicesc
    1.Unorderd
    2.Mutable
    3.No Duplicates
    4.Heterogeneous(It can store different datatypes(immutable only))'''
#How to create set
s1 = {} #This will not create Set, it must require one element otherwise this create DICTIONARY   
s2 = {1,2,3,3,3}
s3 = set([1,23,3,4,4,5])
s4 = set('python')
s5 = set() #this will crate empty set

print(s1, s2, s3, s4, s5)
print(type(s1))

#Demonstarte the how SET is Unordered by iterating the elements
for i in s3:
    print(i)

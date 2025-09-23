# MRO = Method resolution order in python it is use to determine the which method calls first, it is use in Multiple Inheritance to resolve ambiguity.
'''
1. its follows the C3 linearization Algorithm -> Child -> left to right parents -> grandparents -> object
'''
# Single Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

b = B()
b.show()              # Output: B
print(B.mro())        # MRO: [B, A, object]

# Multiple Inheritance
class C:
    def show(self):
        print("C")

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.show()             # Output: B (B comes before C in MRO)
print(D.mro())       # MRO: [D, B, A, C, object]

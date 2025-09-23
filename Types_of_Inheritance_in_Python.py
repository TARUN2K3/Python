# Types of Inheritance in Python
'''
1. Single Inheritance : one child Class inherit from one parent class
2. Multiple Inheritance : one Child class inherit form more than one parent class.
3. Multilevel Inheritance : one child class inherit from parent class and that one parent class inherit form grand parent class.
4. Hierarchical Inheritance : more than one child class inherit form single parent class.
5. Hybrid Inheritance : Combination of two or more type of Inheritance (Multiple + Multilevel)
'''
# Single Inheritance
# class parent:
#     def __init__(self):
#         print("Its a parent class")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("it's a child class")

# c = child()

# # Multiple Inheritance

# class Father:
#     def __init__(self):
#         print("it's a Father class")
# class Mother:
#     def __init__(self):
#         print("It's a Mother calss")
# class child(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#         print("It's a Child class")

# c = child()

# Multilevel Inhertance
# class granparent:
#     def __init__(self):
#         print("its a Grand parent class")
# class parent(granparent):
#     def __init__(self):
#         super().__init__()
#         print("its a parent class")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("its a child class")

# c = child()

# Hierarchical inheritance
class parent:
    def __init__(self):
        print("its a parent calss")
class child1(parent):
    def __init__(self):
        parent().__init__()
        print("its a child1 class")
class child2(parent):
    def __init__(self):
        parent().__init__()
        print("its a child2 class")
class child3(parent):
    def __init__(self):
        parent().__init__()
        print("its a child3 class")
c1 = child1()
c2 = child2()
c3 = child3()
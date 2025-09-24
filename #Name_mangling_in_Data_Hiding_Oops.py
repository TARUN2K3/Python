#Name_mangling_in_Data_Hiding_Oops
'''
we can Access private variable using getter method or Name Mangling way
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def show(self):
        print(f"Marks of the {self.name} is {self.__marks}")

obj = Student("Tarun",91)
obj.show()
print("Access using name mangling:",obj._Student__marks)
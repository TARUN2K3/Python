# Polymorphism in Python
'''
Polymorphism: its means many form.
    same function name but different bhaviour.
    we can achive polymorphism in python by method overriding and ducktyping.
    
'''
class Bird:
    def fly(self):
        return "Bird can FLY"
class Sparrow(Bird):
    def fly(self):
        return "Sparrow can FLY"
class Penguin(Bird):
    def fly(self):
        return "Penguin can't FLY"

b = [Sparrow(),Penguin()]
for i in b:
    print(i.fly())
        
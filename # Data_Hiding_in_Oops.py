# Data Hiding in Oops
'''
Data Hiding: Data Hiding is the concept of restricting the internal variables and Data outside the class
    Intrection happens through getter and setter methods
    Public
    _prtected (name convention)
    __private
'''
class bank:
    def __init__(self,Accountno):
        self.Accountno = Accountno #Public
obj = bank(287)
print(obj.Accountno)

class student:
    def __init__(self,name):
        self._name=name #Prtected
obj1 = student("Tarun")
print(obj1._name)
        
class student:
    def __init__(self,name):
        self.__name = name

    def getter(self):
        return self.__name
obj2 = student("Tarun")
print(obj2.getter())
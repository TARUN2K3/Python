# what are the four basic principle of oops?

'''There are four Basic Principle of OOps in python that are:
Encapsulation : Binding the all data(variables) and methods(Function) in to single Unit.
    In encapsulation we use _Protected and __Private variable name to restrict direct access.
    Hiding the internal details only shows essential features.'''

class bankaccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
        
    def deposit(self,amount):
        self.__balance += amount

acc = bankaccount(1000)

print("deposit method :", acc.deposit(1000))
print("get_balance method :", acc.get_balance())
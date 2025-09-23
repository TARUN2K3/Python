# can child class Inherit the class and instance variable of the parent class ?

class vechile:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")

class car(vechile):
    def drive(self):
        print(f"{self.brand} is driving on {self.wheels} Wheels")

c = car("Toyota")
c.start()
c.drive()

print(c.brand)
print(c.wheels)
        
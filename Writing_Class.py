class Cuboid:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def surface_area(self):
        return 2*(self.length * self.breadth + self.breadth * self.height + self.height * self.length )
    def volume(self):
        return self.length * self.breadth * self.height
    
c1 = Cuboid(2,3,4)
c2 = Cuboid(5,6,7)
print("Surface Area:",c1.surface_area())
print("surface Area:",c2.surface_area())


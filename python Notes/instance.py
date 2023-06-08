# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
    
#     def Perimeter(self):
#         return 2*(self.length+self.breadth)
    
#     def Area(self):
#         return self.length*self.breadth

# x = Rectangle(100,200)
# x.Perimeter()
# x.Area()

# example2

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        
    def Perimeter(self):
        return 2*self.pi*self.radius

    def Area(self):
        return 2*self.pi*self.radius**2
c=Circle(10)
print(c.Perimeter())
print(c.Area())
c1=Circle(20)
print(c1.Area())
print(c1.Perimeter())
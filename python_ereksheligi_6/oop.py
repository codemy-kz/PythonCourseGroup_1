class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.height+self.width)

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

r1 = Rectangle(20, 10)
r2 = Rectangle(15, 3)
r3 = Rectangle(20, 10)

print(r1 > r2)
print(r1 == r3)

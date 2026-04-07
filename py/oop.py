#Inheritance

class Shape: #parent class
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
class Circle(Shape): #Child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle") #super().__init__ creates variables belonging to the class in the bracket.
        self.radius=radius #This means that class 'Shape' does not have radius, but class Circle does.

    def area(self): #override parent method
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side=side #same case for Square with side, but circle does not have side. Only Square.
        #Conversely, Square does not have radius, only circle.

    def area(self):
        return self.side ** 2
    
def print_area(shape):
    print(f"{shape.name} area: {shape.area()}")

#Both circle and square inherit 'name' attribute from Shape
circle = Circle(5)
square = Square(4)

shapes = [Circle(5), Square(6), Circle(3)]
# print(circle.name)
# print(square.name)
# print_area(circle)
# print_area(square)

for shape in shapes:
    print_area(shape)
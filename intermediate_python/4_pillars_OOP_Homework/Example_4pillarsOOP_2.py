from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side:float):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, base:float, height:float):
        self.base = base
        self.height = height
        
    def calculate_perimeter(self):
        return (2 * self.base) + (2 * self.height)

    def calculate_area(self):
        return self.base * self.height


circle_shape = Circle(radius=58)
print(f"The Circle Perimeter is: {circle_shape.calculate_perimeter():.2f}")
print(f"The Circle Area is: {circle_shape.calculate_area():.2f}")

square_shape = Square(side=84)
print(f"The Square Perimeter is: {square_shape.calculate_perimeter()}")
print(f"The Square Area is: {square_shape.calculate_area()}")

rectangle_shape = Rectangle(base=84, height=62)
print(f"The Rectangle Perimeter is: {rectangle_shape.calculate_perimeter()}")
print(f"The Rectangle Area is: {rectangle_shape.calculate_area()}")
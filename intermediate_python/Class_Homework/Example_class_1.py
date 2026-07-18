class circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416

    def get_area(self):
        area = self.pi * (self.radius**2)
        print(area)


radius = int (input("Enter the radius of the circle: "))
calculation_area = circle(radius)
calculation_area.get_area()
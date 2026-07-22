class Circle():
    def __init__(self, radius:float):
        self.radius = radius
        self.pi = 3.1416

    def get_area(self):
        area = self.pi * (self.radius**2)
        return area


calculation_area = Circle(radius=62)
print(f"{calculation_area.get_area():.2f}")
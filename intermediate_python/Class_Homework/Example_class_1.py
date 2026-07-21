class Circle():
    def __init__(self):
        self.radius = 52
        self.pi = 3.1416

    def get_area(self):
        area = self.pi * (self.radius**2)
        return area


calculation_area = Circle()
total_area = calculation_area.get_area()
print(total_area)
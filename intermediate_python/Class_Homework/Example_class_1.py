class circle():
    radius = 0
    pi = 3.1416

    def get_area(self, radius):
        self.area = self.pi * (radius**2)
        print(self.area)


calculation_area = circle()
calculation_area.radius = int (input("Enter the radius of the circle: "))
calculation_area.get_area(calculation_area.radius)
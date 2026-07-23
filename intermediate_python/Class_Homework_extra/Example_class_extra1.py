class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("There is a negative value; the values ​​must be positive")
        self.width = width
        self.height = height


    def get_area(self):
            area = self.width * self.height
            print(f"The Area of your Rectangle is: {area}\n")
            return area


    def get_perimeter(self):
            perimeter = (2 * self.width) + (2 * self.height)
            print(f"The Perimeter of your Rectangle is : {perimeter}\n")
            return perimeter


def main():
    try:
        width_area = int (input("Enter the Width of your Rectangle: "))
        height_area = int (input("Enter the Height of your Rectangle: "))
        print()
        figure = Rectangle(width_area, height_area)
        figure.get_area()
        figure.get_perimeter()
    except ValueError as error:
        print(f"Error: {error}\n")


if __name__ == "__main__":
    main()
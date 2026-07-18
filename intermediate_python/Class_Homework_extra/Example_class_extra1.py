class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        if not (self.width < 0 or self.height < 0):
            self.area = self.width * self.height
            print(f"The Area of your Rectangle is: {self.area}\n")
        else:
            print("Error try to get your Area")
            print(f"You enter a negative value, the Value must to be Positive\n")

    def get_perimeter(self):
        if not (self.width < 0 or self.height < 0):
            self.perimeter = (2 * self.width) + (2 * self.height)
            print(f"The Perimeter of your Rectangle is : {self.perimeter}\n")
        else:
            print("Error try to get your Perimeter")
            print(f"You enter a negative value, the Value must to be Positive\n")


def main():
    width_area = int (input("Enter the Width of your Rectangle: "))
    height_area = int (input("Enter the Height of your Rectangle: "))
    print()
    figure = Rectangle(width_area, height_area)
    figure.get_area()
    figure.get_perimeter()


if __name__ == "__main__":
    main()



from abc import ABC, abstractmethod


class Vehicle ():
    def __init__(self, brand: str, year: int):
        self._brand = brand
        self.__year = year

    @property
    def brand (self) -> str:
        return self._brand

    @brand.setter
    def brand (self, new_brand: str):
        self._brand = new_brand

    @property
    def year (self) -> int:
        return self.__year

    @year.setter
    def year (self, new_year: int):
        if new_year < 1886:
            raise ValueError("Invalid year for a vehicle; vehicles began to be manufactured in 1886")
        self.__year = new_year

    @abstractmethod
    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year, doors: int):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return (f"The {self.brand}, was Manufactured on {self.year} and the numbers of doors is {self.doors}\n")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type: str):
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        return (f"The {self.brand}, was Manufactured on {self.year} and the Type of the Motorcycle is {self.type}\n")


def main():
    vehicle1 = Car("Toyota",2024, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Sport")
    print(vehicle1.get_info())
    print(vehicle2.get_info())

if __name__=="__main__":
    main()




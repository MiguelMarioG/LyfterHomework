class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Bus:
    def __init__(self):
        self.max_passengers = 8
        self.passengers = []  

    def manage_passengers(self):
        while True:
            print("\n==============================================================")
            print(f"Passengers on Board: {len(self.passengers)} out of  {self.max_passengers}")
            choice = input("Do you want to Add (a), Remove (r) or Exit (e)?: ").lower()

            if choice == "e":
                print("Exiting the Bus Control System")
                break

            elif choice == "a":
                if len(self.passengers) >= self.max_passengers:
                    print("We're sorry, the bus is completely Full")
                else:
                    passenger_name = input("Enter the Passenger's Name: ")
                    new_passenger = Person(passenger_name)
                    self.passengers.append(new_passenger)
                    print(f"{passenger_name} has boarded the Bus")

            elif choice == "r":
                if len(self.passengers) == 0:
                    print("The Bus is already Empty")
                else:
                    removed_passenger = self.passengers.pop()
                    print(f"The Passenger {removed_passenger.name} has gotten off the Bus")
            
            else:
                print("Invalid Option. Try Again")


def main():
    my_bus = Bus()
    my_bus.manage_passengers()
    if not my_bus.passengers:
        print("Thanks to Use the System, GoodBye!!")
    else:
        print("\nPassengers who stayed on the Bus:")
        for person in my_bus.passengers:
            print(f"- {person.name}")


if __name__ == "__main__":
    main()
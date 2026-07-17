class Bus():
    max_passengers = 8
    passengers= []

    def add_passengers(self):
        while True:
            print("==============================================================")
            choice = input ("Do you want to add a passenger or remove a passenger (a or r): ")
            if choice == "a":
                self.passenger = input("Enter the name of your Passenger: ")
                self.passengers.append(self.passenger)
                if len(self.passengers) >= self.max_passengers:
                    print("Your Bus is full, sorry")
                    break
            elif choice == "r":
                if len(self.passengers) == 0:
                    print("Your Bus is empty")
                    continue
                else:
                    self.passengers.pop()
                    print(f"The last passenger: {self.passenger} got off the bus")


rtd_bus = Bus()
rtd_bus.add_passengers()
print(rtd_bus.passengers)
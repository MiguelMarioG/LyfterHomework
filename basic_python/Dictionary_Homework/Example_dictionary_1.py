print("-----------Hotel Input-----------")
print()
hotel_name = input("Whats the name of the Hotel: ")
hotel_rating = int(input("Whats the star rating of the Hotel: "))
print()

hotel_dictionary = {
    "name": hotel_name,
    "star_rating": hotel_rating,
    "rooms": []
    }

opt = "y"

while opt == "y":
    print("-----------Hotel Rooms Input-----------")
    print()
    room_number = int (input("Whats the room number: "))
    floor_number = int (input("Whats the floor number: "))
    price_per_night = float (input("Whats the price per night: $"))
    hotel_rooms = {
        "number": room_number,
        "floor": floor_number,
        "price": price_per_night
    }
    hotel_dictionary ["rooms"].append (hotel_rooms)

    opt = (input("Wants to add another room information (y/n): "))
print()
print ("-----------Hotel Information-----------")
print()
print (hotel_dictionary)
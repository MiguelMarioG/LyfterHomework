my_pets_list = [
	'dog',
	'cat',
]

#for index in range (500, 651):
my_pets_list.append('rabbit')
print(my_pets_list)

print()

courses_list = [
	'Computers',
	'Algorithms',
	'Python',
	'Web Development',
]

courses_list.insert(2, 'Databases')
print(courses_list)

print()

first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list)
print(first_list)

print ()

milky_way_planets = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Pluto',
	'Jupiter',
	'Saturn',
	'Uranus',
	'Neptune',
]

for index, planet in enumerate(milky_way_planets):
    if (planet == "Jupiter"):
        deleted_planet = index

deleted_item = milky_way_planets.pop(deleted_planet)
print(milky_way_planets)
print(f'Deleted item: {deleted_item}')
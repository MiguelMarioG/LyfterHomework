my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for record in my_favorite_records:
    if record == 'Fear of a Blank Planet':
        print(f"This is for real {record}")
    else:
        print(f'Record: {record}')


print()


my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index in range(0, len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')


print()

my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

index = 0
while (index < len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')
	index += 1


print()


my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index, record in enumerate(my_favorite_records):
	print(f'Record {index + 1}: {record}')


print()


colors = [
	'black',
	'yellow',
	'red',
	'blue',
]

for color in colors:
	if color == 'yellow':
		continue

	print(color)
def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('The number is to low')
	elif number > 100:
		raise ValueError('The number is to high')
	
	return True

def main():
	number = input('Enter your number: ')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except ValueError as ex:
		print(ex)


if __name__ == '__main__':
	main()
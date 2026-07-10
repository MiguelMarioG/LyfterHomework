def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('El numero es muy bajo')
	elif number > 100:
		raise ValueError('El numero es muy alto')
	
	return True

def main():
	number = input('Ingrese un numero')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except ValueError as ex:
		print(ex)


if __name__ == '__main__':
	main()
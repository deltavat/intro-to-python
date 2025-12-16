def number_range(number):
	if number < 0:
		print(f'{number} is less than 0')
	elif 0 <= number <= 50:
		print(f'{number} is between 0 and 50')
	elif 51 <= number <= 100:
		print(f'{number} is between 51 and 100')
	else:
		print(f'{number} is greater than 100')

number_range(101)
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

#	age = int(input('How old are you? '))
#	print()
#	print(f'You are {age} years old.')
#	print(f'In 10 years, you will be {age + 10} years old.')
#	print(f'In 20 years, you will be {age + 20} years old.')
#	print(f'In 30 years, you will be {age + 30} years old.')
#	print(f'In 40 years, you will be {age + 40} years old.')

age = int(input('How old are you? '))
print()

print(f'You are {age} years old.')

for year in range(10, 50, 10):
	print(f'In {year} years, you will be {year + age} years old.')
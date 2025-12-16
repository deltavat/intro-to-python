# . In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
	1, 3, 6, 11,
	4, 2, 4, 9,
	17, 16, 0,
]

oddities = []

for numbers in my_list:
	if numbers % 2 == 0:
		oddities.append('Even')
	else:
		oddities.append('Odd')
		
from pprint import pprint
pprint(oddities)
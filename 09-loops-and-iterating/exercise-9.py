# Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:



def factorial(n):
	val = 1
	for number in range(1, n + 1):
		val *= number
	return val

print(factorial(6))
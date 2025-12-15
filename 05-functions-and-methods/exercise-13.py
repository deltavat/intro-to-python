# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
	print(first)
	print(second)
	print(third)
	
foo(42)

# It gives an error due to a missing third argument and a default not being defined for the third parameter, as it was for the 2nd.
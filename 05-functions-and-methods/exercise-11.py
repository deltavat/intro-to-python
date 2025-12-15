# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
	print(first)
	print(second)
	print(third)
	
foo(42)

# It prints 42 3 2, using the default values for the second and third paramaters due to insufficient arguments being passed to the function.
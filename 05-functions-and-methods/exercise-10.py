# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
	print(first)
	print(second)
	print(third)
	
foo(42, 3.141592)

# It prints 42 4.141592 2 as it uses the default value for the missing third argument.
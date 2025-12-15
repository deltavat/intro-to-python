# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
	print(first)
	print(second)
	print(third)
	
foo(42, 3.141592, 2.718)

# prints the values in the argument as default values weren't needed to be used due to sufficient values being passed to the function.
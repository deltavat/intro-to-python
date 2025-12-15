# What happens when you run the following program? Why do we get that result?

def set_foo():
	foo = 'bar'
	
set_foo()
print(foo)

# NameError as foo is assigned inside the function set_foo()
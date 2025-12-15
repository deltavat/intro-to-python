# What does this program print? Why?

foo = 'bar'

def set_foo():
	foo = 'qux'
	
set_foo()
print(foo)

# foo is assigned 'bar' globally, foo is assigned 'qux' inside the function set_foor() but stays inside it, so the program eventually prints 'bar' as the value remains unchanged. foo inside set_foo() is a shadow variable.
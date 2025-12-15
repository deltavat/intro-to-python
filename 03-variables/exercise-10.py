# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd'		# reassign
obj.upper()			# none
obj = obj.lower()	# reassign
print(len(obj))		# none
obj = list(obj)		# reassign
obj.pop()			# mutate
obj[2] = 'X'		# mutate
obj.sort()			# mutate
set(obj)			# none
obj = tuple(obj)		# reassign
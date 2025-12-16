# What will the following code print?

print('abc-def'.isalpha())		# False due to '-'
print('abc_def'.isalpha())		# Flase due to '_'
print('abc def'.isalpha())		# False due to ' '
print('abc def'.isalpha() and
	'abc def'.isspace())		# False
print('abc def'.isalpha() or
	'abc def'.isspace())		# False
print('abcdef'.isalpha())		# True
print('31415'.isdigit())		# True
print('-31415'.isdigit())		# False due to '-'
print('31_415'.isdigit())		# False due to '_'
print('3.1415'.isdigit())		# False due to '.'
print(''.isspace())				# Flase
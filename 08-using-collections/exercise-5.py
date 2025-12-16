# Which of the following values can't be used as a key in a dict object, and why?

# Only hashable and immutable objects can be used as keys for a dict:


['a', 'b']						# unhashable/mutable, can't be used
{'a': 1, 'b': 2}				# unhashable/mutable, can't be used
{1, 4, 9, 16, 25}				# unhashable, can't be used
# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The difference in results is due to the first version using the newly sliced string to search from the right, while the second version uses the original string and searches from the right.
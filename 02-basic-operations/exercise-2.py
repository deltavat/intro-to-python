# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

digits =  4936

one = digits % 10
tens = digits % 100 // 10
hundreds = digits % 1000 // 100
thousands = digits % 10000 // 1000

print(thousands, hundreds, tens, one)
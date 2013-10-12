# Loops
# Loop through data and manipulate or print it a certain number of times

for i in range(0, 100):
	print i

# What is i?
# i is basically the number 0, 1, 2, 3, ..., 100
# i will change value every time it gets to the bottom of
# all the lines that have been indented are are inside "it"

for i in range(0, 10):
	print (i * 10)

# Oops I forgot to teach you math
# so math in Python is pretty simple
# Addition
print (1 + 2)
# Multiplication
print (1 * 2)
# Division
print (2 / 2)
# Substraction
print (3 - 2)
# WTF?
print (2 - 3) - (2 - 1 - 2 - 3 - 2 - 1 - 2 - 2 - 3 + 2) * (2 * 2 * 2) / 4
# FIX THIS
print (2 - 3) - ((2 - 1 - 2 - 3 - 2 - 1 - 2 - 2 - 3 + 2) * ((2 * 2 * 2) / 4))

# Exponents!
print 2 ** 2

# Make kind of sense?
# now lets do some math

def math_func(number):
	for i in range(0, 100):
		print number + i

math_func(23)
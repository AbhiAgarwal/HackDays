# Conditional Statements

# A conditional statement is a statement that allows you to check 
# for conditions on data.
# The resulting outcome is dependent on the statement after the "if":
# "if" is true or false
# so
# if abhis_age > 16:
# 	he can drive
# else:
# 	he cannot drive
# We mainly concentrate on the statement "abhis_age > 16"
# where abhis_age is a variable defined

# For example, I have a variable with a number, and I want to test if the number is
# Greater than 5. What do I do?

variable = 5

if (variable > 5):
	print "Number is greater than 5!!"
else:
	print "Number is NOT greater than 5"

# On that note: everything in Python has to have a tab if its inside
# another statement. So because you are printing after the statement:
# if variable > 5: you must tab the next line to show that you're inside
# that section.

# This allows the machine to understand that this particular line or 
# particular lines are inside the "if statement" or the "else" statement

# We can also use Booleans in this format

rightornot = False

if rightornot == True:
	print "This will always be true"
else:
	print "It cant ever be false unless you make heyBool = False"

'''
In Python you make comparisons by using ==
The ONE equals operator is when you want to set something to a variable name
so:

heyBool = True
is making the variable heyBool EQUAL True

BUT:
heyBool == True
is CHECKING if the variable heyBool is EQUAL to True

The same way we can do:
'''

calculation = "+"

if calculation == "+":
	1 + 1
elif calculation == "-":
	1 -1
elif calculation == "*":
	1 * 1
elif calculation == "/":
	1 / 1
else:
	print "I dont understand your input"

# and the same with numbers

myNumber = 23

if myNumber == 23:
	print "My favorite number is {0}".format(myNumber)
else:
	print "No my favorite number is actually " + str(myNumber)

# When you want to convert a number to display as a string
# you have to use the str() function, which will then
# go and convert that number to display it as a String.

myT = 2129
print str(myT) # just print myT WILL NOT WORK..
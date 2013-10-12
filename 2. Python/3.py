# What is a variable?
# Variables are just a store of information. 

hello = "Hello"

username = "Batman"
password = 293019232

pythonString = "Awesome!"
pythonString2 = 'sdkosd'
pythonNumber = 2
pythonNumber2 = "52"
pythonBoolean = True
pythonFloat = 12.34519832
pythonDecimal = 42.5

variablename = "float"
variablename = 2
variablename = 2.5

# What do these things mean?

'''

whatev = "Awesome", basically means that you're putting the STRING 
"Awesome" into the keyword pythonString

then if you do something like "print pythonString" it will print!

'''

what = "Hello World"

print what

print pythonString # see?

# You've to notice something. It has to be EXACTLY THE SAME. It can't be:
# pythonstring, or pYtHoNsTrInG or PYTHONSTRING. Just NO.

'''

pythonNumber = 2 basically means that you're putting the INTEGER
2 into the keyword pythonNumber

You're able to create these imaginary and awesome keywords so you don't 
have to keep repeating the same thing.

For example if I want to do: username = "Abhi",
then I can just always call username and it'll give me "Abhi" instead of 
typing out manually "Abhi" each time!

'''

# Moreover, you can always change them as well!
# Lets try it:

hello_variable = "goodbye"

print hello_variable

pi = 3.14159265

print 2 * pi
print 2 * 3.1415

print # creates a blank line :)
print "Before Change:"
print pythonString
pythonString = "whatup y'all I changed form"
print "After Change:"
print pythonString

# See it's super easy!

# If you want to know what TYPE something is. So if something is an INTEGER
# or if they are a STRING or the other types Python has you can do:

whatisthis = "String"

print
print type(pythonString) # and it'll print out!
print type(pythonNumber)

# Now lets create many strings!

stringOne = "Hi!"
stringTwo = "My"
stringThree = "name"
stringFour = "is"
stringFive = "Abhi!"

# How can I print them all? Just like adding numbers!

print stringOne + stringTwo + stringThree + stringFour + stringFive

print one_string

# ew they print out "Hi!mynameisAbhi!" not "Hi! my name is Abhi!"
# to fix that you can do:

print stringOne, stringTwo, stringThree

print (stringOne + " " + stringTwo + " " + 
	   stringThree + " " + stringFour + " " + stringFive)

print (stringOne + " name is abhi")

# Now they are "Hi! My name is Abhi!" 
# Here you learnt two things: The formatting, and using two lines for the
# same print
# When you're using two lines to print you always have to put it inside
# brackets print ("Hi", new line, "Hi :)")

# OR! you can also use this:

print ("{0} {1} {2} {3} {4}").format(stringOne, stringTwo, stringThree, stringFour, stringFive)

print ("hello my name is {0}, {1}")

# That just says that for {0}, {1}, ... replace them with the stringOne,
# stringTwo, etc ... 
# In most programming languages sequence usually start with 0 rather than 1
# Like you're used to in mathematics, you usually start n with 1,
# but here it's always with 0.

# Lets practice a bit :)
# Print for me:
# 1) Python Rocks in one String
# 2) My Name is {YOUR NAME} all saved in different variables
# 3) CHALLENGE: The number 23 and a string with it!

print "my favorite number is " + str(23)
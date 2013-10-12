# Functions
# A function is a way to group lines of code together as
# either you're trying to repeat lines of code or you're 
# doing it for the sake of simplicity

number = number * 2 + 2 * 6 / 12312302

def printhello():
	variablename = "hello"
	print variablename + " Function!"

# Functions are cool
# Then you call it using function_name

printhello()

# Pretty easy right?
# How do I take in values you ask?

def function_value(hello_world):
	print hello_world

# WOW you can actually do this:
function_value("omg")
# AND IT WORKS!!!!!

# Lets practice
def do_some_math(number):
	number = number * 2
	print number + 8940182390281309812

do_some_math(59902020102)

# the "NUMBER" inside the do_some_math(number) is called a parameter
# It's what you give in the function to do some magical things with it
# You can do pretty cool things with it

def hi_hack_days(name):
	print ("Hi my name is {0} and I am at HackDays").format(name) 

hi_hack_days("Jack")

def plane_joke(name):
	print ("What shouldn't you say on the plane? Hi {0}!").format(name)

plane_joke("Jack")
# hah?
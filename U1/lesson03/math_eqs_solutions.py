# Math equations python script

# import math
# https://docs.python.org/3/library/math.html

from math import pi
# FROM -  imports a subset or even specific methods from that module
# IMPORT - imports the module X creates a reference

# def - defines a function in python
# pass - nothing happens -- passes that function

def area_of_circle():
	radius = eval(input("Enter the radius:"))
	area = pi*(radius**2)
	# How would you use this with str.format()?
	print("The area of a circle with radius {:.3f} is {:.3f}".format(radius, area))
	print("The area of a circle with radius %s is %s" % (radius, area))

def pass_function():
	pass
	
	
def main():
	area_of_circle()
	pass_function()

main()
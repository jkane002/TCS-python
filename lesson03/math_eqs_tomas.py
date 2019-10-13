# Math equations python script

# import math
# https://docs.python.org/3/library/math.html

from math import pi
# FROM -  imports a subset or even specific methods from that module
# IMPORT - imports the module X and creates a reference

# def - defines a function in python
# pass - nothing happens -- passes that function

def area_of_circle():

	radius = input("what is the radius of your circle")
	area = radius*radius*pi
	print("the area of your circle is", area)
	pass

def main():
	area_of_circle()

main()

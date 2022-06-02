# Mary Mederos
# 11/07/2019
# Homework Assignment 7
# This program uses turtle graphics to render an image.

import math
from turtle import Turtle		# Instantiate Turtle object class.

# Square shape
def square(t, length):
	"""Draws a square with the given length."""
	for count in range(4):
		t.forward(length)
		t.left(90)

# Hexagon shape
def hexagon(t, length):
	"""Draws a hexagon with the given length."""
	for count in range(6):
		t.forward(length)
		t.left(60)

# Radial Pattern
def radialPattern(t, n, length, shape):
	"""Draws a radial pattern of n shapes with the given length."""
	for count in range(n):
		shape(t, length)
		t.left(360 / n)

# Declare the main function.
def main():
	t = Turtle()
	t.pencolor("red")
	t.hideturtle()
	t.width(2)
	radialPattern(t, n = 8, length = 80, shape = square)
	t.clear()
	t.pencolor("blue")
	radialPattern(t, n = 15, length = 50, shape = hexagon)

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
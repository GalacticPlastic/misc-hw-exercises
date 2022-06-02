# Mary Mederos
# 11/29/2019
# Homework Assignment 7
# This program uses turtle graphics to render an image.

import math
from turtle import Turtle		# Instantiate Turtle object class.

# Circle shape
def drawCircle(t, x, y, radius):
	"""Draws a circle with the given center point and radius."""
	t.up()
	t.goto(x + radius, y)
	t.setheading(90)
	t.pencolor("yellow")
	t.down()
	for count in range(120):
		t.speed(12)
		t.left(3)
		t.forward(2.0 * math.pi * radius / 120.0)

# Draws a rectangle shape with the given length and width.
def rectangle(t, length, width):
	t.forward(length)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.forward(length)
	t.left(90)
	t.forward(width)

# Square shape
def square(t, length):
	"""Draws a square with the given length."""
	for count in range(4):
		t.forward(length)
		t.left(90)

# Hexagon shape
def hexagon(t, length):
	"""Draws a hexagon with the given length."""
	t.pencolor(47, 86, 233)
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
	t.hideturtle()
	t.speed(12)

	radialPattern(t, 15, 50, hexagon)

	t.begin_fill()
	t.fillcolor("yellow")
	drawCircle(t, 0, 0, 20)
	t.end_fill()
	t.up()

	t.home()
	t.setheading(270)
	t.goto(0, -20)
	t.forward(80)

	t.down()
	t.begin_fill()
	t.fillcolor("green")
	rectangle(t, 150, 10)
	t.end_fill()

	t.up()
	t.setheading(275)
	t.forward(65)
	t.setheading(145)

	t.begin_fill()
	t.fillcolor("green")
	square(t, 40)
	t.end_fill()

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
# Mary Mederos
# 11/07/2019
# Homework Assignment 7
# This program uses turtle graphics to render an image.

from turtle import Turtle		# Instantiate Turtle object class.
import random

# Draws a rectangle shape with the given length and width.
def rectangle(t, length, width):
	t.forward(length)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.forward(length)
	t.left(90)
	t.forward(width)

def moveTurtle(t, x, y, degree, distance, length, width):
	t.up()
	t.goto(x, y)
	t.setheading(degree)
	t.forward(distance)
	t.down()
	t.begin_fill()
	t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	rectangle(t, length, width)
	t.end_fill()

# Declare the main function.
def main():
	t = Turtle()
	t.speed(3)

	# Loop to draw random rectangles
	for count in range(10):
		t.width(random.randint(1, 4))

		moveTurtle(
			t,
			random.randint(0, 100),
			random.randint(0, 100),
			random.randint(0, 360),
			random.randint(20, 100),
			random.randint(30, 200),
			random.randint(30, 200)
		)


# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
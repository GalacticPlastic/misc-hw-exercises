# Mary Mederos
# 11/05/2019
# In Class Lab #8
# This program uses turtle graphics to render an image of a bullseye.

from turtle import Turtle		# Instantiate Turtle object class.
import random

# Declare the main function.
def main():
	t = Turtle()
	t.speed(10)
	t.home()
	
	# Loop to draw random rectangles
	for i in range(5):
		t.hideturtle()
		t.up()
		t.sety((30*(6-i))*(-1))
		t.down()
		t.showturtle()
		t.begin_fill()
		t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		t.circle(30*(6-i))
		t.end_fill()

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
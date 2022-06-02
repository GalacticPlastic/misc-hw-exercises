# Mary Mederos
# 09/12/2019
# Homework Assignment 2
# This program calculates the area of a circle.

# Import the math module.
from math import pi

# Calculate the square root of an input.
def circleArea(r):
    area = pi * (r ** 2)
    rounded_area = round(area, 2)
    print("The area of your cicle is " + str(rounded_area) + ".\n")

# Request the input.
def main():
    diameter = input("Enter the Diameter of Your Cicle: ")
    radius = int(diameter) / 2
    circleArea(int(radius))

# Invoke the main function.
if __name__== "__main__":
  main()

# Prompt user to exit program.
input('Press Any Key to Quit')

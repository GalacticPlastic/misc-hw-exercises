# Mary Mederos
# 09/12/2019
# In Class Lab #2
# This program will take 3 integers and display the square root of each one.

# Import the math module.
from math import sqrt

# Calculate the square root of an input.
def mySquareRoot(num):
    square_root = str(sqrt(num))
    print("The square root is " + square_root + ".\n")

# Request the inputs
def main():
    print("This program will take 3 integers and display the square root of each one.\n")

    first_integer = input("Enter First Integer: ")
    mySquareRoot(int(first_integer))

    second_integer = input("Enter Second Integer: ")
    mySquareRoot(int(second_integer))

    third_integer = input("Enter Third Integer: ")
    mySquareRoot(int(third_integer))

# Invoke the main function.
if __name__== "__main__":
  main()

# Prompt user to exit program.
input('Press Any Key to Quit')

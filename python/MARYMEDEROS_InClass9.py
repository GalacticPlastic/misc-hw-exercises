# Mary Mederos
# 11/07/2019
# Homework Assignment 9
# This program ...

import random

def getGuess():
	getGuess = int(input("Enter Your Guess: "))
	return getGuess

def checkNum(num, guess):
	if guess < num:
		print("The number you guessed is too small.")
	elif guess > num:
		print("The number you guessed is too big.")
	else:
		print("Wow, you guessed it. You win!")

# Declare the main function.
def playGame():
	num = random.randint(1, 100)
	print("I'm thinking of a number between 1 and 100. Try to guess it.")

	guess = getGuess()
	count = 0
	while not checkNum(num, guess):
		count += 1
		guess = getGuess()

# Invoke the main function.
playGame()

# Prompt user to exit program.
input('Press Any Key to Quit')
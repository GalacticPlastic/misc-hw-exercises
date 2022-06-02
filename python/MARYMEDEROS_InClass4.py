# Mary Mederos
# 09/26/2019
# In Class Lab #4
# This program takes a user's age and outputs their legal abilities at that age.

# Import random library:
import random

# Request the inputs.
def main():
    age = int(input("How old are you?\n"))
    
    if age >= 25:
        print("You can do pretty much anything!")
    elif age >= 18:
        print("You can vote but not rent a car.")
    elif age >= 16:
        print("You can drive but not vote.")
    else:
        print("You can't drive.")

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
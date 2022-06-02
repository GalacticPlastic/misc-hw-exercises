# Mary Mederos
# 09/19/2019
# Homework Assignment 3
# This program receives a string input and returns the formatted index and value of each character on a new line.

# Request the string input.
def main():
    word = input("Enter a word: ")

    for index, character in enumerate(word):
        i = index + 1
        print("%10d %10s" % (i, character))

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')

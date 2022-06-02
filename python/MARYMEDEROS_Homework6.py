# Mary Mederos
# 10/24/2019
# Homework Assignment 6
# This program receives text from a file and then
# alphabetizes each unique occurrence of a word.

# Declare the main function.
def main():
	file = open("datafile.txt", 'r')	# Reads file content. No write permissions.
	data = file.read().split()

	# The sorted function orders the list.
	# The set class returns only unique elements.
	print(sorted(set(data)))

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
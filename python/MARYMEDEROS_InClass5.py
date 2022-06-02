# Mary Mederos
# 10/03/2019
# In Class Lab #5
# This program opens a file and prints the number of four-letter words in it.
# Expected total is 10 (not including the last word, because of the question mark character).

# Declare the main function.
def main():
	counter = 0.0		# Tally the total amount of words with 4 characters.

	file = open("datafile.txt", 'r')	# Reads file content. No write permissions.
	data = file.read().split()

	for word in data:
		if len(word) == 4:
			counter += 1
			# print(word)

	print("Total number of words with 4 characters: ", int(counter))

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
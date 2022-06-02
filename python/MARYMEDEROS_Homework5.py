# Mary Mederos
# 10/17/2019
# Homework Assignment 5
# This program will modify the string input of a user.

# Declare the main function.
def main():
	word = input("Enter a Word: ")
	full_sentence = input("Enter a Sentence: ")
	
	split_sentence = full_sentence.split(" ")

	print('a)'.ljust(5) + full_sentence.upper())
	print('b)'.ljust(5) + str(full_sentence.count(word)))
	print('c)'.ljust(5) + full_sentence.replace(word, 'big'))
	print('d)')

	for word in split_sentence:
		print(word)

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
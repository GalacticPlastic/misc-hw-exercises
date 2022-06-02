# Mary Mederos
# 10/17/2019
# In Class Lab #6
# This program .

# Declare the main function.
def main():
	fortunes = [
		"If you eat something and no one sees you eat it, it has no calories.",
		"You do not have to be faster then the bear. Just faster then the slowest guy running from it.",
		"Ask not what your fortune can do for you, but what you can do for your fortune.",
		"The road to riches is paved in homework.",
		"Read the Docs.",
		"Linters are your friend."
	]
	number = int(input("Enter a number from 1 to 6: "))

	fortune = str(fortunes[number - 1])

	print("Your fortune is:\n" + fortune)

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
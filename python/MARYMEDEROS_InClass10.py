# Mary Mederos
# 11/14/2019
# In Class 10
# This program converts miles to kilometers.

import random

def doConversion(mile_input):
	km_output = mile_input * 1.609
	return round(km_output, 2)

# Declare the main function.
def main():
	print("%10s%18s" % ("miles", "kilometers"))
	for i in range(10):
		km_output = doConversion(i)
		print("%10d%18.2f" % (i, km_output))

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
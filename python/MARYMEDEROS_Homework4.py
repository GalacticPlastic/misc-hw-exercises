# Mary Mederos
# 09/26/2019
# Homework Assignment 4
# This program takes user inputs and prints the sum of the numbers and their average.

# Declare the main function.
def main():
  sum = 0.0       # Set sum variable to zero prior to for loop.
  
  print("\nEnter a series of numbers to calculate the total sum and average of all numbers entered (separate with space).\nPress enter to quit.\n")
  user_input = input("Enter a number: ")

  # Split the numbers entered using space as the separator.
  data = user_input.split(" ") 
  
  for number in data:
    sum += float(number)

  # Output total for all numbers entered.
  print("Sum: ", sum)
  
  average = sum / len(data)
  print("Average: ", average)

# Invoke the main function.
main()

# Prompt user to exit program.
input('Press Any Key to Quit')
# Mary Mederos
# 09/12/2019
# In Class Lab #3
# This program is a counting machine that takes an input of a number to count up to
# and an input of a number to count by. It outputs all numbers up to and including that number.

# Request the inputs
def main():
    print("This program is a counting machine.\n")
    start = int(input("Enter what number you would like the computer to start at: "))
    stop  = int(input("Enter what number you would like the computer to count to: "))
    step  = int(input("Enter what number you would like the computer to count by: "))

    for number in range(start, stop + 1, step):
        print(number, end = "\n")

# Invoke the main function.
if __name__== "__main__":
  main()

# Prompt user to exit program.
input('Press Any Key to Quit')

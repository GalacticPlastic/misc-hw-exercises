# Mary Mederos
# 09/05/2019
# In Class Lab #1

# Request the inputs
def main():
    name = input("Enter Your Name: ")
    print("Hello, " + name + ".\n")

    age = input("How old are you? ")
    print("You are " + str(age) + ".\n")

    years_until_100 = 100 - int(age)
    print("You will be 100 in " + str(years_until_100) + " years.\n")

# Invoke the main function.
if __name__== "__main__":
  main()

# Prompt user to exit program.
input('Press Any Key to Quit')

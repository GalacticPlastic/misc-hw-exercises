# Mary Mederos
# 09/05/2019
# Homework Assignment 1
# This program will convert kilometers to miles.
# 1km = 0.621371 miles
# Please debug this code and get it working properly.

# Request the input.
def main():
   print("This program will convert kilometers to miles.\n" )

   kilometers = input("Enter the number of kilometers: ")
   miles =  float(kilometers) * 0.621371

   print(str(kilometers) + " kilometers is equal to " + str(miles) + " miles.\n")

# Invoke the main function.
if __name__== "__main__":
  main()

input("Press any key to exit program.")

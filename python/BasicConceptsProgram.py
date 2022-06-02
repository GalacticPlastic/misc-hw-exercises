#these are comments when the program is run they are ignored they are for humans reading the code
#on your programs don't forget to enter you name here
#assignment number
#date

#It is a good programming practice to put all your code inside a function in this case called main
def main():

    #this is the input section of the program.
    #users will be able to enter values
    #save them to an identifier/variable so that you can use the values later
    stringEntered = input("Enter a word or phrase here")
    intEntered = int(input("Enter an integer here"))
    floatEntered = float(input("Enter a float (decimal value) here"))

    #this is a for loop the loop will be run the number of times the user entered
    for i in range(intEntered):
        #you would enter all code that needs to be repeated here
        print("This is the number ", i, "time through the loop")

    #this is the output section of the program the results will displayed in this section using print statements
    #the next line prints a blank line on the screen
    print()
    print("The string you entered will be displayed on the next line")
    print(stringEntered)
    print("The float value you entered rounded to 2 decimal places is, ", round(floatEntered,2))

#The next line calls the main function you created above and actually runs that ode
main()

#The next line is needed so that when you double click on the program the window will remain open
input("Press enter to exit program")

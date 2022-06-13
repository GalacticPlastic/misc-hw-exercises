/*methodExample1.java
 * 10/21/19
 * This program demonstrates how to define and invoke some simple
 * void and value-returning methods.
 */

import java.util.Scanner;

public class methodExample1 {

	public static void main(String[] args) 
	{	//declare and initialize variables
		String userColor;
		String userLetter;
		
		double userGrade1 = 0.0, userGrade2 = 0.0, userGrade3 = 0.0;
		double userAverage = 0.0;
		
		Scanner in = new Scanner(System.in);
		
		//call(invoke)
		displayIntro(); //stand-alone statement
		
		//call favoriteColor
		//test with a string literal
		displayFavoriteColor("blue"); //"blue" is the argument that is passed to the paramter color

		//test displayFavoriteColor with a variable
		//prompt the user for a color
		System.out.print("Enter your favorite color: ");
		userColor = in.nextLine();
		
		//call displayFavoriteColor
		displayFavoriteColor(userColor);
		
		//call getTestGrade 3 times and store the result 
		//in userGrade1, userGrade2, userGrade3
		userGrade1 = getTestGrade();
		userGrade2 = getTestGrade();
		userGrade3 = getTestGrade();
		
		//call average to calculate the average of the user's
		//grades
		userAverage = average(userGrade1, userGrade2, userGrade3);
		
		//call average to display the average of 5, 8, and 9
		System.out.println("\nthe average of 5, 8 and 9 = "+ average(5,8,9));
		
		//display userAverage to test
		System.out.println("\nYour average = " + userAverage);
		
		//call letterGrade to store the user's letter in userLetter
		userLetter = letterGrade(userAverage);
		
		//invoke displayInfo
		displayInfo(userColor, userAverage, userLetter);
		
	}
	
	//define methods
	
	//return type: void 
	//parameters: None
	//purpose: This method displays an introduction.
	public static void displayIntro()
	{
		System.out.println("WELCOME TO THE METHOD EXAMPLE PROGRAM!!\n\n");
	}
	
	//return type: void 
	//parameters: 1 string (color)
	//purpose: This method displays the user's favorite color
	public static void displayFavoriteColor(String color)
	{
		System.out.println("Your favorite color is " + color);
	}
	
	//return type: double
	//parameters: None
	//purpose: This method prompts the user for a test grade and 
	//validates that the grade is between 0 and 100
	public static double getTestGrade()
	{
		Scanner userin = new Scanner(System.in);
		
		//local variable
		double grade = 0.0;
		do
		{
		//prompt for grade
		System.out.print("Enter a grade between 0 and 100: ");
		grade = userin.nextDouble();
		
		//validate 0 - 100
		if (grade < 0 || grade > 100)
		{
			//display invalid
			System.out.println("Invalid.  You must enter 0 -100.\n");
			
		}
		}
		while (grade < 0 || grade > 100);
		
		return grade;
	
		
	}
	
	//return type: double
	//parameters: 3 doubles (x, y, z)
	//purpose: This method returns the average of x, y and z
	public static double average(double x, double y, double z)
	{
		return (x + y + z) / 3.0;
	}
	
	//return type: String
	//parameter: double(numGrade)
	//purpose: This method returns the letter grade
	//that corresponds to the given numeric grade.
	public static String letterGrade(double numGrade)
	{
		if (numGrade >= 90)
		{
			return "A";
		}
		else if(numGrade >= 80)
		{
			return "B";
		}
		else if(numGrade >= 70)
		{
			return "C";
		}
		else if(numGrade >= 60)
		{
			return "D";
		}
		else
		{
			return "F";
		}
	}

	//return type: void
	//parameter:  String(color),  double (avg), String (letter)
	//purpose: This method displays the user's info
	public static void displayInfo(String color, double avg, String letter)
	{
		System.out.println("Favorite Color:\t\t" + color);
		System.out.println("Numeric Average:\t" + avg);
		System.out.println("Letter Grade \t\t" + letter);
		
	}
	
}

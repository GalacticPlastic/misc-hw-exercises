//method_classwork.java
//Names: Mary Mederos and Sam Mark, and Kameron Rogers (?)
// November 4, 2019
// 25 points

import java.util.Scanner;
import java.lang.Math;

public class methodClasswork {

	public static void main(String[] args) {
		double userRadius = 0.0, userVolume = 0.0, userArea = 0.0;
		
		// call the GetRadius method (2 pts)
		userRadius = GetRadius();
		
		// call the CalculateVolume method (2 pts)
		userVolume = CalculateVolume(userRadius);
		
		// call the CalculateArea method (2 pts) 
		userArea = CalculateArea(userRadius);
	
		// call the DisplayResults method (2 pts)
		DisplayResults(userRadius, userVolume, userArea);
		
		// call the DisplayFarewell method (2 pts)
		DisplayFarewell();
	}
	
	//return type: double
	//parameters: none
	//purpose: This method prompts the user for the radius of a sphere,
	//validates that it is positive and returns the value.
	//(3 pts)
	public static double GetRadius()
	{
		double radius = 0.0;
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the radius of a sphere: ");
		radius = userInput.nextDouble();
		
		// Validation:
		do {
			if (radius < 0) {
				System.out.print("Invalid entry. Please enter a positive number.");
			}
			return radius;
		} while(radius < 0);
		
		
	}
		
	//return type: double
	//parameters: 1 double(radius)
	//purpose: This method returns the volume of the sphere with the given radius.
	//V = 4/3πr^3
	//(3 pts)
	public static double CalculateVolume(double radius)
	{
		double volume = 0.0;
		volume = 1.3333 * Math.PI * Math.pow(radius, 3);
		
		return volume;
	}

	//return type: double
	//parameters: 1 double(radius)
	//purpose: This method returns the surface area of the sphere with the give radius
	//V = 4πr^2
	//(3 pts)
	public static double CalculateArea(double radius)
	{
		double area = 0.0;
		area = 4 * Math.PI * Math.pow(radius, 2);
		
		return area;
	}
	
	//return type: void
	//parameters: 3 doubles(radius, volume, area)
	//purpose: This method displays the radius, volume and surface area of sphere as follows:
	//Radius: 		10 units
	//Volume:		4188.8 cubic units
	//Surface Area: 1256.6 square units
	//(3 pts)
	public static void DisplayResults(double radius, double volume, double area)
	{
		System.out.println(
			"\nRadius:\t\t" + radius + " units\n"
			+ "Volume:\t\t" + volume + " cubic units\n"
			+ "Surface Area:\t" + area + " square units\n"
		);
	}
	
	//return type: void
	//parameters: none
	//purpose: This method displays a farewell message to the user as follows:
	//Have a nice day!!
	//(3 pts)
	public static void DisplayFarewell()
	{
		System.out.println("Have a nice day!!");
	}
}
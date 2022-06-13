/*methodPracticeworksheet.java
 * 10/21/19
 * This program demonstrates some simple void and value-returning
 *methods.
 */
import java.util.Scanner;

public class methodPracticeworksheet {

	public static void main(String[] args) {
		int day =0, month = 0, yr = 0;
		double userCircleArea = 0.0, userRadius = 0.0;
		
		
		Scanner in = new Scanner(System.in);
		//call(invoke) printDate
		System.out.println("Testing printDate...\n");
		System.out.println("Today's date is: ");
		printDate(10,21,2019);
		
		
		//prompt the user for day, month and yr
		System.out.print("\nEnter your birthday day: ");
		day = in.nextInt();
		System.out.print("Enter your birthday month: ");
		month = in.nextInt();
		System.out.print("Enter your birthday yr: ");
		yr = in.nextInt();
		
		System.out.println("\nYour birthday is: ");
		printDate(day, month, yr);
		
		System.out.println("\n\nTesting circleArea...\n");
		//display the area of a circle with radius 5
		System.out.println("The area of a circle with radius 5 = " + circleArea(5));
		//prompt for userRadius
		System.out.print("Enter the radius of a circle: ");
		userRadius = in.nextDouble();
		
		//call circleArea to store in userCircleArea
		userCircleArea = circleArea(userRadius);
		
		//display for testing
		System.out.println("\nuserCircleArea = " +userCircleArea);
		
	}

	//method definitions
	//return type: void
	//parameters: 3 ints (d, m, y)
	//purpose: This method displays a date
	public static void printDate(int d, int m, int y)
	{
		System.out.print(d + "/" + m + "/" + y);
	}
	
	//return type: double
	//parameters: 1 double(radius)
	//purpose: This method returns the area of the given circle.
	public static double circleArea(double radius)
	{
		return 3.14 * radius * radius;
	}
	
}

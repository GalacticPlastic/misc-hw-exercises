/* grades.java
 * Mary Mederos
 * October 21, 2019
 * This program reads grades from a file and sorts them by a predefined scale. */

/* Algorithm:
 * Declare variables
 * String file;
   int totalAs =  0;
   int totalBs =  0;
   int totalCs =  0;
   int totalDs =  0;
   int totalFs =  0;
   
   Declare a File object.
   Declare a Scanner object to read from the file.
   Read from file and loop through lines.
   For each line, determine the grade letter the integer amounts to,
   then add to the total sum for that letter grade.
   Once the loop is done, print the totals for each letter grade.
   Close file.
 */

// Import Libraries
import java.util.Scanner;				// Needed to do any input in your program.
import javax.swing.JOptionPane;	// Pop up a standard dialog box that prompts users for a value.
import java.io.*;								// Needed to read and write files.

public class grades {
  public static void main(String[] args) throws IOException
  {
    // Declare and initialize variables and constants.
    int totalAs =  0;		// Accumulator, initialized to 0.
    int totalBs =  0;		// Accumulator, initialized to 0.
    int totalCs =  0;		// Accumulator, initialized to 0.
    int totalDs =  0;		// Accumulator, initialized to 0.
    int totalFs =  0;		// Accumulator, initialized to 0.
    
    // First confirm that the file exists.
    File file = new File("grades.txt");
    if (!file.exists())
    {
      System.out.println("The file grades.txt is not found.");
      System.exit(0);
    }

    // Open the file for reading.
    Scanner inputFile = new Scanner(file);
    
    // Read the file contents into the array.
    while (inputFile.hasNext())
    {
      // Read the next line.
      int grade = inputFile.nextInt();

      if (grade > 89)
      {
        // Add the grade to the total number of As.
        totalAs += 1;
      }
      else if (grade > 79)
      {
        // Add the grade to the total number of Bs.
        totalBs += 1;
      }
      else if (grade > 69)
      {
        // Add the grade to the total number of Cs.
        totalCs += 1;
      }
      else if (grade > 59)
      {
        // Add the grade to the total number of Ds.
        totalDs += 1;
      }
      else {
        // Add the grade to the total number of Fs.
        totalFs += 1;
      }
    }

    // Display the totals for each letter grade.
    System.out.println("Total As:" + totalAs);
    System.out.println("Total Bs:" + totalBs);
    System.out.println("Total Cs:" + totalCs);
    System.out.println("Total Ds:" + totalDs);
    System.out.println("Total Fs:" + totalFs);

    // Close the file.
    inputFile.close();
	}
}

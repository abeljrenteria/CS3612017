/**
 * @author Christelle
 * 
 */
import java.io.*;
import java.util.*;

public class ScannerDemo {

	private static String file1 = "/Users/abeljrenteria/eclipse-workspace/ParseScanner/src/prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println(file1);
		
		Token t;

		while (!ts.isEndofFile()) {
			t = ts.nextToken();
			t.toString();
			System.out.println("Token "+ counter + ": " + t.getType() + "\t" + "Type: " + t.getValue());
			counter = counter + 1;
			
		}
	}
}

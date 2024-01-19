package shippingPriceCalc;
import java.util.*;

public class Calculator {

	public static void main(String[] args) {
		
		        // Constants for shipping rates
		        final double BASE_RATE = 5.0;
		        final double RATE_PER_KG = 2.0;

		        // Get package weight from the user
		        Scanner scanner = new Scanner(System.in);
		        System.out.print("Enter the weight of the package in kilograms: ");
		        double weight = scanner.nextDouble();

		        // Calculate shipping cost
		        double shippingCost = calculateShippingCost(weight, BASE_RATE, RATE_PER_KG);

		        // Display the result
		        System.out.println("Shipping cost for a " + weight + " kg package: Rs. " + shippingCost);

		        // Close the scanner
		        scanner.close();
		    }

		    // Function to calculate shipping cost
		    private static double calculateShippingCost(double weight, double baseRate, double ratePerKg) {
		        return baseRate + (weight * ratePerKg);


	}

}

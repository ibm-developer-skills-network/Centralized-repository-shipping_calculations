# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the claculator package weight in kilograms: "))
rate = float(input("Enter the calculator shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")


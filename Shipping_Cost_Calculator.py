# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight(kg): "))
rate = float(input("Enter the shipping rate (per kg): "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

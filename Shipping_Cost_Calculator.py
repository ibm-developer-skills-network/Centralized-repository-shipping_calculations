# Shipping Cost Calculator

## Initialize variable configurations
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display total calculations result
print(f"Total Shipping Cost: {shipping_cost} USD")

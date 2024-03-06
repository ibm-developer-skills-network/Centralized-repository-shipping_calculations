# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
if (weight>50):
    print("Impossivel entregar")
else:
    shipping_cost = weight * rate
    ## Display the result
    print(f"Shipping Cost: {shipping_cost} USD")


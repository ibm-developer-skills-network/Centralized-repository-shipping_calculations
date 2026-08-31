# Shipping Cost Calculator
# Here is a new update by MinhTiHon ngu qua troi
## Input package weight and shipping rate
weight = float(input("Enter the package weight in Tan: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate*1.5

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")


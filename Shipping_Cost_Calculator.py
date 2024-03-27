# Shipping Cost Calculator

# Here is a new update by LebogangMadisha

git config --global user.email "lebogang.madisha@imseismolgy.org"
git config --global user.name "lebogang.madisha"

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")


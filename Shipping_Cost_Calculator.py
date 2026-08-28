# Shipping Cost Calculator

## Input package weight, volume dimensions, and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
length = float(input("Enter the package length in centimeters: "))
width = float(input("Enter the package width in centimeters: "))
height = float(input("Enter the package height in centimeters: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate volumetric weight
volumetric_weight = (length * width * height) / 5000

## Choose the greater between actual and volumetric weight
if volumetric_weight > weight:
    chargeable_weight = volumetric_weight
else:
    chargeable_weight = weight

## Calculate final shipping cost
shipping_cost = chargeable_weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost:.2f} USD (based on {chargeable_weight:.2f} kg)")
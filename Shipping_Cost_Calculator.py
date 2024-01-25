# Shipping Cost Calculator

# Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate shipping cost
shipping_cost = weight * rate

# Apply a discount if the package weight is greater than 10 kilograms
if weight > 10:
    discount = 0.10  # 10% discount
    shipping_cost -= shipping_cost * discount

# Display the result
print(f"Shipping Cost: {shipping_cost} USD")

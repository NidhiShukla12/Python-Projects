

# 1. Calculate the area of a circle.

import math

# Define the radius
radius = 8

# Function to calculate the area of a circle
def calculate_area_of_circle(radius):
    # Calculate the area using the formula π * r^2
    area = math.pi * (radius ** 2)
    return area

# Calculate the area
area = calculate_area_of_circle(radius)

# Print the result
print(f"The area of the circle with radius {radius} is: {area:.2f}")

# output will be = 201.06
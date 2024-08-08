
# 2.Calculate the area of a triangle

import math

# Define the base and height
base = 20
height = 40

# Function to calculate the area of a triangle
def calculate_area_of_triangle(base, height):
    # Calculate the area using the formula (1/2) * base * height
    area = 0.5 * base * height
    return area

# Calculate the area
area = calculate_area_of_triangle(base, height)

# Print the result
print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")

# output will be = 400
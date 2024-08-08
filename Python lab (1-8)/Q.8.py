
# 4.Calculate the area of a square.

import math

# Function to calculate the area of a square
def calculate_area_of_square(side):
    # Calculate the area using the formula side^2
    area = side ** 2
    return area

# Define the side length
side = 4

# Calculate the area
area = calculate_area_of_square(side)

# Print the result
print(f"The area of the square with side length {side} is: {area:.2f}")

# output will be = 16.00
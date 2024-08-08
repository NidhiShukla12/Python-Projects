
#3.Calculate the area of a rectangle.

import math

# Function to calculate the area of a rectangle
def calculate_area_of_rectangle(length, width):
    # Calculate the area using the formula length * width
    area = length * width
    return area

# Define the length and width
length = 8
width = 5

# Calculate the area
area = calculate_area_of_rectangle(length, width)

# Print the result
print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")

# output will be = 40
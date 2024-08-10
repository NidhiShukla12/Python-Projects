
# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

# Taking input from user
num = float(input("Enter a number: "))

# Check if the number is even or odd using conditional statement
result = "Even" if num % 2 == 0 else "Odd"

# Print the result
print(f"The number is {result}.")
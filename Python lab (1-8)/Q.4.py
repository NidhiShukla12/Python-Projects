
# Q.4 Write a program to calculate greatest of three numbers.


# Define three numbers
number1 = 10
number2 = 25
number3 = 20

# Determine the greatest number using if-elif-else statements
if number1 >= number2 and number1 >= number3:
    greatest = number1
elif number2 >= number1 and number2 >= number3:
    greatest = number2
else:
    greatest = number3

# Print the result
print("The greatest number is:", greatest)

# Hence get the output 25.



# 2nd method

# Define three numbers
number1 = 10
number2 = 25
number3 = 20

# Find the greatest number using max()
greatest = max(number1,number2,number3)

# Print the result
print("The greatest number is:", greatest)
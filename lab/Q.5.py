
# 5.Write a Python program that determines the largest of three numbers entered by the user.


# Get user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
   print("the largest number is ", num1)
if num2 >= num1 and num2 >= num3:
   print("the largest number is ", num2)
else:
   print("the largest number is ", num3)


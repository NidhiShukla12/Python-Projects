
# 2. Using input function take two number and then swap the number.


# 1st method using the third variable

# Take two numbers as input from the user

num1 = float(input('enter the first number', ))
num2 = float(input('enter the second number', ))

# swap the numbers with using the third variable

temporary = num1
num1 = num2
num2 = temporary

# print the swapped numbers

print(num1)
print(num2)

# 2nd method without third variable

# Take two numbers as input from the user

num1 = float(input('enter the first number', ))
num2 = float(input('enter the second number', ))

# swap the two numbers

num1 , num2 = num2 , num1

# print the swapped numbers

print(num1)
print(num2)

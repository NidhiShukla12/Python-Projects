
# 3.Write a Python program that determines if a given year is a leap year or not.


# Get user input for year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year is a leap year.")
else:
    print("year is not a leap year.")
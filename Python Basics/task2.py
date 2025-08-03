# Input data
input_year = int(input("Enter the year: "))

# Defining the year
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print("It's a leap year")
else:
    print("It's a normal year")
# Input data
width = float(input("Enter the width (см): "))
length = float(input("Enter the length (см): "))
height = float(input("Enter the height (см): "))

# Checking the conditions for the selection of packaging
if width <= 15 and length <= 15 and height <= 15:
    print("Box #1")
elif width > 200 or length > 200 or height > 200:
    print("Ski packaging")
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print("Box #2")
else:
    print("Box #3")
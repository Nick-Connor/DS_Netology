ticket_number = input('Enter the six-digit ticket number: ')

# Check that 6 digits are entered
if len(ticket_number) != 6:
    print("Error: you need to enter exactly 6 digits")
else:
# Splitting the number into the first and last three digits
# Record [:3] and [3:] are slices of strings (or lists) that allow you to get a part of the sequence.
    first_part = ticket_number[:3]
    second_part = ticket_number[3:]

# Counting the sum of the digits in each part
# int(digit) in Python is a construct that converts a string consisting of digits into an integer
sum_first = sum(int(digit) for digit in first_part)
sum_second = sum(int(digit) for digit in second_part)

# Check the condition of the "lucky" ticket
if sum_first == sum_second:
    print("Lucky ticket!")
else:
    print("Unlucky ticket")
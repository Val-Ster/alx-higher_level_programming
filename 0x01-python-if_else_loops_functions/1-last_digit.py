#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Check if d number is -ve or +ve as u get d last digit of d num
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
# Determine the condition based on the last digit
if last_digit > 5:
    condition = "and is greater than 5"
elif last_digit == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"
# Print the result
print(f"Last digit of {number} is {last_digit} {condition}")

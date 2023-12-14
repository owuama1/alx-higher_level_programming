#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Determine the sign of the number and get the last digit
sign = -1 if number < 0 else 1
last_digit = abs(number) % 10 * sign

# Print the required output
print(f"Last digit of {number} is {last_digit} and is", end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print(f"less than 6 and not 0")

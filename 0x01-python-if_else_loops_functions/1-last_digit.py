#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
# YOUR CODE HERE
last_digit = number % 10

# Check if the last digit is greater than 5
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
# Check if the last digit is 0
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
# Otherwise, the last digit is less than 6 and not 0
else:
    print(f"Last digit of {number} is -{last_digits} not is less than 6and not 0")

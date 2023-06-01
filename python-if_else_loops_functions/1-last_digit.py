#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    nm = number % -10
else:
    nm = number % 10
if nm > 5:
    print(f"Last digit of {number} is {nm} and is greater than 5")
elif nm == 0:
    print(f"Last digit of {number} is {nm} and is 0")
elif nm < 6 and nm != 0:
    print(f"Last digit of {number} is {nm} and is less than 6 and not 0")

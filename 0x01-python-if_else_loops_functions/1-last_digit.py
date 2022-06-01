#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tempNum = 0

if number < 0:
	tempNum = number * -1

lastDigit = tempNum % 10
result = "Last digit of {:d} is {:d} and is {}"

if lastDigit > 5:
	result = result.format(number, lastDigit, "greater than 5")
elif lastDigit == 0:
	result = result.format(number, lastDigit, "0")
elif lastDigit < 6 and lastDigit != 0:
	result = result.format(number, lastDigit, "less than 6 and not 0")

print(result)

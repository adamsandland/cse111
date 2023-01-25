"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
# Import libraries to make the calculation
import math

# Prompt the user for the Pendulum Length
pendLength = float(input("Enter the length of the Pendulum in Meters:"))

if pendLength > 4:
    for i in range(2):
        print("WOW, that's LOOOOOOONG")


if pendLength>2:
    print("WOW, that's LOOOOOOONG")


# Calculate the time in seconds
calculation = round((2 * math.pi * math.sqrt(pendLength/9.81)), 2)

# Display the time as a nice number for the user (rounded to the first two decimals)
print('The time it takes to make one full swing is ' + str(calculation)+ ' in seconds.')
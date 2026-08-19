# Aim: To use basic built-in Python modules such as random, statistics, and 
# math to perform random, statistical, and mathematical operations.

import random
import statistics
import math


print("----- RANDOM MODULE -----")

# Generate a random integer
number = random.randint(1, 100)
print("Random number:", number)

# Generate a random floating-point number
decimal = random.random()
print("Random decimal:", decimal)

# Select a random item from a list
students = ["Rahul", "Priya", "Amit", "Neha"]

winner = random.choice(students)

print("Randomly selected student:", winner)

# Statistics Module

marks = [80, 75, 90, 85, 70, 80]

print("----- STATISTICS MODULE -----")

print("Marks:", marks)

print("Mean:", statistics.mean(marks))

print("Median:", statistics.median(marks))

print("Mode:", statistics.mode(marks))

print("Standard Deviation:", statistics.stdev(marks))


# Math Module

print("----- MATH MODULE -----")

number = 25

print("Square root:", math.sqrt(number))

print("Power:", math.pow(2, 3))

print("Factorial:", math.factorial(5))

print("Value of PI:", math.pi)

print("Ceiling:", math.ceil(4.3))

print("Floor:", math.floor(4.8))
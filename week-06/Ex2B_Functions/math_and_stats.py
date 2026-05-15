# Import modules
import random
import math
import statistics

# Create values from 1-99
vals_1_100 = range(1, 100)

# Random sample of 75 unique values
vals_sample = random.sample(vals_1_100, 75)

# Random selection of 200 values (duplicates allowed)
vals_choices = random.choices(vals_1_100, k=200)

# Random radius between 3 and 10
radius = random.randint(3, 10)

# Store value of pi
pi = math.pi

# Calculate circle area
area = pi * radius ** 2

# Print first section
print("_Experimenting with a subset of integers 1-100:")

print("Sum of 75 sample values from 1 to 100:",
      math.fsum(vals_sample))

print("Average of 75 sample values:",
      statistics.mean(vals_sample))

print("Median of 75 sample values:",
      statistics.median(vals_sample))

# Line break
print('\n')

# Print second section
print("_Experimenting with a superset of 200 values, integers 1-100:")

print("Average of 200 values:",
      statistics.mean(vals_choices))

print("Median of 200 values:",
      statistics.median(vals_choices))

print("Mode of 200 values:",
      statistics.mode(vals_choices))

print("Standard deviation of 200 values:",
      statistics.stdev(vals_choices))

print("Variance of 200 values:",
      statistics.variance(vals_choices))

# Line break
print('\n')

# Print third section
print("_Modeling a random circle:")

print("Radius =", radius,
      ", area =", math.ceil(area),
      "(rounded up to the nearest integer)")

print("Radius =", radius,
      ", area =", math.floor(area),
      "(rounded down to the nearest integer)")
# MULTI-PARAMETER FUNCTIONS
def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65))


""" in is a python keyword """

# RECURSION - technique where a function invokes itself 
""" Best examples: 1. Factorials
2. Fibonacci Numbers """ 

## NOTE: Recursive calls consume a lot of memory

# QUESTIONS:
# CODE 1:
"""def factorial(n):
    return n * factorial(n - 1)
print(factorial(4))"""
## O/P: RecursionError: maximum recursion depth exceeded), as there is no base case the function has no termination

# CODE 2:
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25))
# O/P :56


## BUILT-IN FUNCTIONS --- should be treated as keywords and these can be overwritten too..
# Find the max of a list of numbers
max_val = max(1, 2, 3)
print(f"The max value is {max_val}")
# Find the min of a list of numbers
min_val = min(1, 2, 3)
print(f"The min value is {min_val}")
# Get the length of a string
text = input("Enter some text: ")
print(f"The length of \"{text}\" is {len(text)}") 


## TYPE-CONVERSION FUNCTIONS -- Comparing between incompatible types will result in error
""" Python has many built-in functions that convert between data types
These are int, float, str, bool , list"""
# Try entering a number and text
val = input("Enter a number: ")
val_int = int(val)
print(f"The value of {val} is {val_int}")
# Converting an integer type to float will truncate the decimal value
float_val = 3.14
int_val = int(float_val)
print(f"The value of {float_val} is {int_val}")
# Converting a number to a string also has its uses
big_number = 184759372934
big_number_str = str(big_number)
print(f"There are {len(big_number_str)} digits in {big_number_str}")

# MATH FUNCTIONS -- MATH module contains many useful functions for mathematical operations
import math
signal_power = 10
noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(f"The decibel value is {decibels}")
# The math module also has a function to convert from radians to degrees
radians = 0.7
degrees = math.degrees(radians)
print(f"{radians} radians is {degrees} degrees")
# The math module also has a function to convert from degrees to radians
degrees = 45
radians = math.radians(degrees)
print(f"{degrees} degrees is {radians} radians")

# RANDOM NUMBERS --- RANDOM function returns a random number between 0 and 1. "randint" function returns a random interger between two numbers
""" Other Random Functions : randrange, choice, choices, shuffle, sample"""
import random
# Generate 10 random numbers between 0 and 1
for i in range(10):
    print(random.random())
# Generate 10 random integers between 4 and 10
for i in range(10):
    print(random.randint(4, 10))
# Randomly select a value from a list
outcomes = ["rock", "paper", "scissors"]
print(random.choice(outcomes))


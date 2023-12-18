import random

# Welcome the user to our application and tell them what this application is used for
print('Welcome to use our application')
print('Application number 1 is meant for guessing your choice of a number between 1 and 10')
print('Application number 2 is meant for calculating rectangles area for you from random variables between 2-10')

print('Application number 1')
# Generate a random number between 1 and 10 for the user
print('Think of a number between 1 and 10 in your mind')

# Create a random number with this application and print it to the user
guess = random.randint(1, 10)
print(f"Here is the number {guess}.")
print('Did we guess your number correctly?')

print('Application number 2')
# Create a random numbers with this application to be rectangles sides
height = random.randint(2, 10)
width = random.randint(2, 10)

# Use the following formula to calculate rectangles area from random numbers between 2 and 10
# The formula is a * b = c, a = height, b = width and c = area
a = height
print(f"Height of your rectangle is {a}")
b = width
print(f"Width of your rectangle is {b}")
c = a * b
print(f"The Area of rectangle is {c} ")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want!')
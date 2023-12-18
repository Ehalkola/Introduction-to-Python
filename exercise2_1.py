import math

# Welcome the user to the application and explain what this application is for
print('Hello! Welcome to use our application')
print('This application is for calculating the volume of a ball and a box')

# Ask the user the sphere of their choice
sphere = float(input("Enter the sphere/radius"))

# Use the following expression, : V = 4/3 * π * (r ^ 3), V = Ball's volume
V = 'volume_of_the_ball'
r = sphere

# Import the users input data to calculate the volume of the ball
# Calculation for the volume of the ball
volume_ball = float(round(4 / 3 * math.pi * (r * r * r),2))

# Print the final result to the user
print(f"Your input sphere {sphere}, gives your ball the volume of {volume_ball}")

# Ask the user to input height, width, and depth (these are the sides) of the box
height = float(input("Give the height of your box"))
width = float(input("Give the width of your box"))
depth = float(input("Give the depth of the box"))

# Volume of the box = V, V = a * b * c
# a = height, b = width, c = depth
# Use the previous expression ( V = a * b * c) to calculate the volume of the box
volume = float(round(height * width * depth, 2))

# Print the final result to the user
print(f"Here is your box's volume {volume} calculated")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want')

import math

# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application!')
print('In this application you can calculate the hypotenuse with the side a and b.')

# Ask the user the length of triangles sides
# Ask the user the length of side a
print('Side A is the left side of the triangle from the corner.')
side_a = float(input("Input the side A, of the triangle"))

# Ask the user the length of side b
print('Side B is the right side of the triangle from the corner')
side_b = float(input('Input the side B, of the triangle'))

# Here is the explanation for the following expressions, a^2 + b^2 = c^2, c = math.sqrt(a^2 + b^2)
a = side_a
b = side_b
side_c = 'hypotenuse'

# Use the previous expressions to calculate the hypotenuse of the users triangle
# Calculation for the hypotenuse
hypotenuse = (a ** 2) + (b ** 2)
final_c = float(round(math.sqrt(a ** 2 + b ** 2), 2))

# Print the final result to the user
print(f'Here is your input side_a {side_a}, side_b {side_b} equals hypotenuse of {final_c}.')

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want!')

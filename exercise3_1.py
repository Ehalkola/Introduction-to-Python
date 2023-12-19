# Welcome the user to our application
print('Welcome to use our application')

# User input
number1 = int(input('Give a number'))
number2 = int(input('Give a second number'))

# Printout for the user
if number1 > number2:
    print(f"Here's the bigger number {number1}")
elif number2 > number1:
    print(f"Here's the bigger number {number2}")
elif number1 == number2:
    print("Numbers are equal")

# Thank the user for using our application and welcome them again
print('Thank you for using our application!')
print("You're always welcome to use this application as often and as much as you want.")
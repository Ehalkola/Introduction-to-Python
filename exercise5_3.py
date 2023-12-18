import math

# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application')

# Create variable, which defines when loop runs
run = True
# Create a loop, which asks user radius of circle to calculate it`s area, printout the result in the end
while run is True:
    r = float(input("Give radius of the circle: "))
    circle_area = round(math.pi * r ** 2, 2)
    print(circle_area)
    yes_no = input("Do you want to continue? (y/n) ").lower()
    if yes_no == "y":
        run = True
    else:
        run = False

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want.')
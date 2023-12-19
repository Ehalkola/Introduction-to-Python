# Welcome the user to our application
print('Welcome to use our application')
print('This application is meant to calculate is your input year a leap year')

while True:
    year = int(input("Input your year here, use whole numbers: "))

# Printout rules and printout
    if year > 0:
        break
    else:
        print("Invalid input, please use whole numbers above 0 ")
if year % 4 == 0:
    print("Leap year: YES")
else:
    print("Leap year: NO")

# Thank the user for using our application and welcome them again
print('Thank you for using our application!')
print("You're always welcome to use this application as often and as much as you want.")
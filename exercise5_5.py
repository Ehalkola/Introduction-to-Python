# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application')

# Create tuple, which contains all the months (January, February, March, April, May, June, July
# August, September, October, November, December
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December')

# Create a loop, which asks user a number and prints out month, which matches the number, this loop
# should also determine if number is valid, if valid run = True, if it's not valid run = False
user_input = int(input("Input a number (1- 12): "))
month_number = user_input - 1
month = months[month_number]
if 0 <= month_number < len(months):
    print(f"The month, which matches your number is {month}")

# Thank the user for using our application, and welcome them again
print('Thank you for using our application!')
print('You are always welcome to use this application as often and as much as you want.')

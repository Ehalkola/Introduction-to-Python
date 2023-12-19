# Welcome the user to our application
print('Welcome to use our application')

# User input
temp = float(input('Give a temperature'))

# Printouts and their terms
if temp < -10:
    print('SUPER COLD')
elif temp < 0:
    print('REALLY COLD')
elif temp <= 10:
    print('COLD')
elif temp <= 15:
    print('CHILLY')
elif temp <= 20:
    print('NORMAL')
elif temp <= 25:
    print('WARM')
elif temp <= 30:
    print('HOT')
elif temp > 30:
    print('SUPER HOT')

# Thank the user for using our application and welcome them again
print('Thank you for using our application!')
print("You're always welcome to use this application as often and as much as you want.")